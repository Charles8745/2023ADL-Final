from openai import OpenAI
import json
import time
## Params
api_key = ''
model = "gpt-3.5-turbo" # gpt-3.5-turbo, gpt-4, 
iteration = 5
output_path = "Oak_guidel_Bulbasaur._Dialogue.json"

## Instance OpenAI client
client = OpenAI(api_key=api_key)

## prompt default 
bg1 = "Background: Professor Samuel Oak (Japanese: オーキド・ユキナリ博士 Dr. Yukinari Okido) is a Pokémon Professor and a major supporting character of the Pokémon anime who lives and works at his research lab in Pallet Town. He appears semi-regularly to give Ash Ketchum advice to help him achieve his goal of becoming the greatest Pokémon Master.\n"
bg2 = "Professor Samuel Oak is currently working at the Pokémon Training Center, where his primary task is to guide new Pokémon trainers in selecting their initial Pokémon and introducing them to what Pokémon are.\n"
bg3 = "In the beginning, new trainers have three Pokémon to choose: Bulbasaur, Charmander, and Squirtle.\n"
task = "Please give me 1 dialogue about Professor Oak guiding and introducing new trainers to select Bulbasaur, Charmander, or Squirtle. The Dialogue must be under 150 tokens and diverse. It should be in this format: #trainer#: <fill in>, #Oak#: <fill in>, ..."


prompt = bg1 + bg2 + bg3 + task

## main
response = client.chat.completions.create(
  model=model,
  temperature = 0.7,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

output = response.choices[0].message.content
print(output)