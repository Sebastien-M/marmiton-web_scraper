
import requests
import unicodedata
from bs4 import BeautifulSoup
import pdb

# recherche = input('recherche: ')
recherche = 'tomate'
root_url = 'http://www.marmiton.org'
url = 'http://www.marmiton.org/recettes/recherche.aspx?aqt=' + recherche

html = requests.get(url)
html = str(html.content)
soup = BeautifulSoup(html, "html.parser")
recipes = soup.find_all('a', 'recipe-card')

i = 0
while i < len(recipes):
    recipe_link = root_url + recipes[i]['href']
    recipe_html = requests.get(recipe_link)
    recipe_html = recipe_html.content
    soup2 = BeautifulSoup(recipe_html, "html.parser")
    recipe_name = soup2.title.text.rsplit(':')[0][:-1]
    # personnes = soup2.div['recipe-ingredients__qt-counter']
    nb_person = soup2.find("div", { "class" : "recipe-ingredients__qt-counter"}).input['value']
    # ingredient_list = soup2.findall("li", { "class" : "recipe-ingredients__list__item"})
    pdb.set_trace()
    print(recipe_name)
    print('pour {} personnes\n'.format(nb_person))
    i+=1
