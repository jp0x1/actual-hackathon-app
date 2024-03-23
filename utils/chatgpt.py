from openai import OpenAI
import openai
#setting up the openai key to use chatgpt
client = OpenAI(api_key='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')

#can use both with provided ingredients and generated ingredients

def create_recipe(ingredients, food_name):
    #ingredients is a list, food_Name is a food name
    ingredients_string = ingredients
    print(ingredients_string)
    prompt = f"Create a recipe in steps for {food_name} using these ingredients: {ingredients_string}"
    #create chatgpt response to send to api utilize credits(?) NEED TEST
  
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful nutrional assistant. DO NOT TALK IN FIRST PERSON. Make sure you specify that you cannot be truly trusted. Do not list the ingredients. Just specifically make the steps"},
        {"role": "user", "content": prompt}
    ]
    )
    steps = completion.choices[0].message.content.split('Step')
    steps = [step+'\n' for step in steps]
    return steps
