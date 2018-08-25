import requests
from bs4 import BeautifulSoup

from Recipe import Recipe

recherche = input('recherche: ')
root_url = 'http://www.marmiton.org'
url = 'http://www.marmiton.org/recettes/recherche.aspx?aqt=' + recherche

html = requests.get(url)
html_content = str(html.content)
soup = BeautifulSoup(html_content, "html.parser")
all_recipes = soup.find_all('a', 'recipe-card')


def extract_recipes_data(recipes):
    for recipe_html in recipes:
        recipe_link = root_url + recipe_html['href']
        recipe = Recipe(recipe_link)

        print(recipe.get_recipe_name())
        print('pour {} personnes\n'.format(recipe.get_nb_person()))
        print('Ingredients:')
        for ingredient in recipe.get_ingredients():
            print(ingredient['ingredient_quantity'] + ingredient['ingredient_name'])
        print('\n\n')


extract_recipes_data(all_recipes)
