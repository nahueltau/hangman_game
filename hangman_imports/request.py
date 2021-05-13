
import requests
from html.parser import HTMLParser


class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


def search_word(word):
    headers = {'user-agent': 'Diccionario/2 CFNetwork/808.2.16 Darwin/16.3.0',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': 'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0',
               }
    search = requests.get(
        'https://dle.rae.es/data/search?w='+word, headers=headers)

    response = search.json()
    id = response['res'][0]['id']

    word_def = requests.get(
        'https://dle.rae.es/data/fetch?id='+id, headers=headers)

    filteredHTML = HTMLFilter()

    filteredHTML.feed(word_def.text)
    
    return filteredHTML.text
