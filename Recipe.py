import requests
from bs4 import BeautifulSoup


class Recipe:
    def __init__(self, recipe_link):
        self.recipe_link = recipe_link
        self.recipe_html_content = requests.get(recipe_link).content
        self.recipe_object = BeautifulSoup(self.recipe_html_content, 'html.parser')

    def get_recipe_name(self):
        return self.recipe_object.title.text.rsplit(':')[0][:-1]

    def get_nb_person(self):
        return self.recipe_object.find('div', {'class': 'recipe-ingredients__qt-counter'}).input['value']

    def get_ingredients(self):
        ingredients = self.recipe_object.find_all('li', 'recipe-ingredients__list__item')
        ingredients_list = []
        for ingredient in ingredients:
            ingredient_quantity = ingredient.find('span').text
            ingredient_name = ingredient.find('span', 'ingredient').text
            ingredients_list.append({'ingredient_name': ingredient_name,
                                     'ingredient_quantity': ingredient_quantity})
        return ingredients_list

    def get_recipe_steps(self):
        recipe_steps = []
        steps = self.recipe_object.find_all('li', 'recipe-preparation__list__item')
        for step in steps:
            recipe_steps.append(step.text.split('\t\t\t')[1].split('\t\t')[0])
        return recipe_steps
