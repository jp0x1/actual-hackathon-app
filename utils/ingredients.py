import requests
import json

#define the app_id and app_key as global variables
app_id = '26bb0925'
app_key = 'dca4d71c073769537f8a370dfea80da2'

# queries the database for food that matches the user input
def food_search(query): 
    query_search = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(query, app_id, app_key))
    query_search = query_search.json()
    return query_search["hits"]

# takes the filters the user inputted(user_filter_list) and the food list from the database(food_list)
# and compares the filters and dietlabels and if it matches add it to a final list
def filter_food_items(user_filter_list, food_list):
    search_food_list = []
    # gets every food item index from API food query
    for food in food_list:
        # gets every filter from the inputted filters from form
        for user_filter in user_filter_list:
            # gets the filters from each specific food item
            if user_filter in food['recipe']['dietLabels']:
                # checks if the current filter is in the diet Labels of the current food
                search_food_list.append([food['recipe']['label'], 
                    food['recipe']['image'],
                    food['recipe']['dietLabels'], 
                    food['recipe']['healthLabels'],
                    food['recipe']['ingredientLines'],
                    round(food['recipe']['calories'])])
                # print(search_food_list)
                continue
    return search_food_list
                

def process_no_filter(food_list):
    updated_list = []
    for food in food_list:
        updated_list.append([food['recipe']['label'], 
                    food['recipe']['image'],
                    food['recipe']['dietLabels'], 
                    food['recipe']['healthLabels'],
                    food['recipe']['ingredientLines'],
                    round(food['recipe']['calories'])])
    return updated_list

#CUSTOM INGREDIENTS