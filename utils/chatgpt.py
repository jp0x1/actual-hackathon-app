from openai import OpenAI
import openai
#setting up the openai key to use chatgpt
openai.api_key = "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"
client = OpenAI()
#can use both with provided ingredients and generated ingredients

def create_recipe(ingredients, food_name):
    #ingredients is a list, food_Name is a food name
    ingredients_string = ','.join(ingredients)
    prompt = f"Create a recipe for {food_name} using these ingredients: {ingredients_string}"
    #create chatgpt response to send to api utilize credits(?) NEED TEST
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=50
    )
    return (response.choices[0].text.strip())

