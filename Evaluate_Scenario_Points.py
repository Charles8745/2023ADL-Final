from openai import OpenAI
import json
import time
## Params
api_key = ""
model = "gpt-4" # gpt-3.5-turbo, gpt-4, 
json_path = "Oak_general_Dialogue.json"
output_path = "Oak_general_Dialogue_rating.json"

## Instance OpenAI client
client = OpenAI(api_key=api_key)

## prompt default 
task = 'Oak Task: Guide new Pokémon trainers select their starter Pokémon\n'
rule = 'Rule: On a scale of 1 to 9, where 1 is a purely mundane dialogue(e.g., chit-chat) and 9 is extremely task-related, Evaluate the relevance of the following dialogue to the Oak task. No explanation, just the score number is enough.\n'
# shot = "#trainer#:  #Oak#: \nRating: \n"
shot1 = "#trainer#: Professor Oak, how does the weather affect Pokémon battles? #Oak#: Ah, the weather can have a significant impact on battles! Rain boosts Water-type moves, while harsh sunlight powers up Fire-type moves. Keep an eye on the forecast to gain an advantage!\nRating: 5\n"
shot2 = "#trainer#: Professor Oak, I'm so excited to start my Pokémon journey! Which Pokémon should I choose as my first companion? #Oak#: Ah, the enthusiasm of a new trainer! It depends on your preferences. Grass, Fire, or Water-type Pokémon are common choices. What kind of Pokémon do you feel a connection with?\nRating: 8\n"
shot3 = "#trainer#: Professor Oak, do you have any tips for training Pokémon? I want mine to be the strongest in battles! #Oak#: Training is key! Make sure to battle other trainers, participate in Pokémon battles, and explore. The more your Pokémon battle, the stronger they'll become. Also, don't forget about type advantages in battles!\nRating: 3\n"
shot4 = "#trainer#: Hey Professor Oak, I've heard so much about Pikachu! Is it true that it's an Electric-type Pokémon? #Oak#: Ah, yes! Pikachu is indeed an Electric-type Pokémon. It's a popular choice for many trainers due to its energetic and friendly nature.\nRating: 2\n"
shot5 = "#trainer#: Professor Oak, I heard water-type Pokémon are strong. Should I go for one of those? #Oak#: Water-types can be formidable, but it depends on your strategy. Consider your preferences and the type of Pokémon battles you want to excel in.\nRating: 7\n"
shot6 = "#trainer#: How important is the type advantage in battles? #Oak#: Type advantage is crucial in battles. Consider the gyms you'll face and the types of Pokémon you might encounter on your journey.\nRating: 3\n"
shot7 = "#trainer#:  #Oak#: \nRating: \n"

## main
with open(json_path, "r", encoding="utf-8") as f:
  test_data = json.load(f)

output_list = []

for idx, conversation in enumerate(test_data):
  dialogue = f"#trainer#: {conversation['trainer']} #Oak#: {conversation['Oak']}\nRating: <fill in here>\n"
  # dialogue = f"{conversation['dialogue']}\nRating: <fill in here>\n"
  prompt = task + rule + shot1 + shot2 + shot3 + shot4 + shot5 + shot6 + dialogue

  response = client.chat.completions.create(
    model=model,
    temperature = 0.2,
    messages=[
      {"role": "user", "content": prompt}
    ]
  )

  rating = response.choices[0].message.content
  rating = [item for item in rating if item.isdigit()]

  output_list.append({'id': idx, "task": task, 'trainer': conversation['trainer'], "Oak": conversation['Oak'], "Rating": rating[0]})
  # output_list.append({'id': idx, "task": task, 'dialogue': conversation['dialogue'], "Rating": rating[0]})

  print("\n","-"*20)
  print(f"{idx}")
  # print(f"trainer: {conversation['trainer']}")
  # print(f"Oak: {conversation['Oak']}")
  # print(conversation['dialogue'])
  print(f"Rating: {rating[0]}")
  print("-"*20)
  time.sleep(5)

## save json file
json_file = open(output_path, mode='w', encoding="utf8")
json.dump(output_list, json_file, ensure_ascii=False, indent=2)
print('-'*40, '\n', f'save at {output_path}')  