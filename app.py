from flask import Flask, render_template, redirect, request, flash
from werkzeug.urls import url_quote
from utils.ingredients import food_search, filter_food_items, process_no_filter
from utils.chatgpt import create_recipe
app = Flask(__name__)

def process_check():
    pass

def process_form():
    food_name = request.form.get('food_name')
    food_list = food_search(food_name)
    user_filter_list = request.form.getlist('filter_list')
    if len(user_filter_list) > 0:
        updated_list = filter_food_items(user_filter_list,food_list)
        # print(updated_list)
    else:
        updated_list = process_no_filter(food_list)
    return updated_list, food_name
    #use this for later to route to results
    #return updated_list

@app.route('/custom', methods=["GET", "POST"])
def custom_food():
    if request.method == "GET":
        return render_template('custom.html')
    if request.method  == "POST":
        pass
    
@app.route('/results', methods=['GET', 'POST'])
def food_data():
    if request.method == 'GET':
        return render_template('results.html')
    elif request.method  == "POST":
        food_list, food_name =  process_form()

        return render_template('results.html', food_list = food_list, food_name=food_name)
    
@app.route('/recipe', methods=['GET','POST'])
def recipe():
    if request.method == "GET":
        ingredients = request.args.get('food_ingredients')
        print(ingredients)
        food_name = request.args.get('food_name')
        food_image = request.args.get('image')
        recipe = create_recipe(ingredients, food_name)
        return render_template("recipe.html", food_name=food_name, food_image=food_image, ingredients=ingredients, recipe=recipe)
    
@app.route('/', methods = ["GET", "POST"])
def main():
    if request.method  == "GET":
        return render_template("home.html")

@app.route('/about')
def about():
    pass

if __name__ == "__main__":
    app.secret_key = "super_secret_key"  # Change this to a secure ENCRYPTED key
    app.run(host='0.0.0.0',debug=True)