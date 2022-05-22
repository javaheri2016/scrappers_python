import requests
from bs4 import BeautifulSoup
import time

quotes_url = "https://www.brainyquote.com/topics/page-quotes"
response = requests.get(quotes_url)
soup = BeautifulSoup(response.text, 'html.parser')

i = 1
quotes_list = []
for i in range(17):
    for quote in soup.find_all("div", class_="grid-item"):
        single_quote = dict()

        try:
            single_quote["text"] = quote.find("a", class_="b-qt").text.replace("\n\n", "").replace("\n", "")
        except:
            single_quote["text"] = "no data"

        try:
            single_quote["author"] = quote.find("a", class_="bq-aut").text.replace("\n\n", "").replace("\n", "")
        except:
            single_quote["text"] = "no data"

        quotes_list.append(single_quote)

    i = i + 1
    pageno = "_" + str(i)
    next_page_url = quotes_url + pageno
    response = requests.get(next_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

quotes_list
print("How many items: " + str(len(quotes_list)))
