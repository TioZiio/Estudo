

import requests
from bs4 import BeautifulSoup as bsp

url = 'http://localhost:12000/'

response = requests.get(url)
text_html = response.text

organizado_html = bsp(text_html, 'html.parser')
print(organizado_html.title.text)
print(100 * '_')

jobs = organizado_html.select_one('#intro > div > div > article > h2')
#  Para pegar uma especifica basta apenas ir no codigo fonte e apertar botão direito no item e copiar selletor;
#  #top-3 > div:nth-child(1) > div:nth-child(1) > header:nth-child(1) > h2:nth-child(1)
if jobs is not None:
    print(jobs)
    print(100 * '_')

    article = jobs.parent
    if article is not None:
        print(article)
        print(100 * '_')

        for p in article.select('p'):
            print(p.text)
        print(100 * '_')
