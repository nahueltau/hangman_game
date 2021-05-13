import requests
from html.parser import HTMLParser
from html import unescape
            
def search_word(word):
    headers = {'user-agent': 'Diccionario/2 CFNetwork/808.2.16 Darwin/16.3.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic cDY4MkpnaFMzOmFHZlVkQ2lFNDM0',
            }        
    search = requests.get('https://dle.rae.es/data/search?w='+word, headers=headers)

    r = search.json()
    id = r['res'][0]['id']

    word = requests.get('https://dle.rae.es/data/fetch?id='+id, headers=headers)
    unescaped = unescape(word.text)

    class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
            self.text += data

    f = HTMLFilter()

    f.feed(unescaped)
    return f.text

