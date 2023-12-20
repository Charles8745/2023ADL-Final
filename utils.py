from openai import OpenAI
import json
import time

def rating(log, api_key, model="gpt-4"):
  client = OpenAI(api_key=api_key)

  ## prompt default 
  task = 'Oak Task: Guide new Pokémon trainers select their starter Pokémon\n'
  rule = 'Rule: On a scale of 1 to 9, where 1 is a purely mundane dialogue(e.g., chit-chat) and 9 is extremely task-related, Evaluate the relevance of the following dialogue to the Oak task. No explanation, just the score number is enough.\n'
  ## shot example
  shot1 = "#trainer#: Professor Oak, how does the weather affect Pokémon battles? #Oak#: Ah, the weather can have a significant impact on battles! Rain boosts Water-type moves, while harsh sunlight powers up Fire-type moves. Keep an eye on the forecast to gain an advantage!\nRating: 5\n"
  shot2 = "#trainer#: Professor Oak, I'm so excited to start my Pokémon journey! Which Pokémon should I choose as my first companion? #Oak#: Ah, the enthusiasm of a new trainer! It depends on your preferences. Grass, Fire, or Water-type Pokémon are common choices. What kind of Pokémon do you feel a connection with?\nRating: 8\n"
  shot3 = "#trainer#: Professor Oak, do you have any tips for training Pokémon? I want mine to be the strongest in battles! #Oak#: Training is key! Make sure to battle other trainers, participate in Pokémon battles, and explore. The more your Pokémon battle, the stronger they'll become. Also, don't forget about type advantages in battles!\nRating: 3\n"
  shot4 = "#trainer#: Hey Professor Oak, I've heard so much about Pikachu! Is it true that it's an Electric-type Pokémon? #Oak#: Ah, yes! Pikachu is indeed an Electric-type Pokémon. It's a popular choice for many trainers due to its energetic and friendly nature.\nRating: 2\n"
  shot5 = "#trainer#: Professor Oak, I heard water-type Pokémon are strong. Should I go for one of those? #Oak#: Water-types can be formidable, but it depends on your strategy. Consider your preferences and the type of Pokémon battles you want to excel in.\nRating: 7\n"
  shot6 = "#trainer#: How important is the type advantage in battles? #Oak#: Type advantage is crucial in battles. Consider the gyms you'll face and the types of Pokémon you might encounter on your journey.\nRating: 3\n"
  shot7 = "#trainer#: Can I catch other Pokémon later? #Oak#: Absolutely! Your journey is about discovery. Choose wisely now, but many more adventures await! \nRating: 6\n"
  shot8 = "#trainer#: Professor Oak, I need help deciding. #Oak#: Of course! Choosing a Pokémon is a crucial step. What are your thoughts so far? #trainer#: I like Charmander's determination, but Squirtle's resilience is tempting too. #Oak#: It's a common dilemma. Think about the kind of battles you envision and the type of Pokémon you'd enjoy training. \nRating: 7\n"
  shot9 = "#trainer#: Professor Oak, what's the Pokémon League like? #Oak#: The Pokémon League is the ultimate challenge for trainers. You'll face powerful opponents to prove your skills. #trainer#: I'll train hard and make it to the top! #Oak#: Ambition and determination will take you far. \nRating: 3\n"

  ## main
  prompt = task + rule + shot1 + shot2 + shot3 + shot4 + shot5 + shot6 + shot7 + shot8 + shot9 + "".join(log)

  response = client.chat.completions.create(
    model=model,
    temperature = 0.2,
    messages=[
      {"role": "user", "content": prompt}
    ]
  )

  rating = response.choices[0].message.content
  rating = [item for item in rating if item.isdigit()]

  return rating[0]

def starter_text(dialogue_log):
  dialogue_log.append("-"*20)
  dialogue_log.append("    [A] Bulbasaur")
  dialogue_log.append("    [B] Charmander")
  dialogue_log.append("    [C] Squirtle")
  dialogue_log.append("-"*20)

  print("-"*20)
  print(" "*4, "[A] Bulbasaur")
  print(" "*4, "[B] Charmander")
  print(" "*4, "[C] Squirtle")
  print("-"*20)

  while True:
    choose = input("Please choose a starter: ")

    if choose == "A":
      choose = "Bulbasaur"
      break

    elif choose == "B":
      choose = "Charmander"
      break

    elif choose == "C":
      choose = "Squirtle"
      break

  return choose, dialogue_log