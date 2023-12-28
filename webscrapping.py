from pip._vendor import requests
from bs4 import BeautifulSoup

URL = "https://www.x-rates.com/table/?from=USD&amount=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

data = []
table = soup.find('table', attrs={'class':'tablesorter ratesTable'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values


def convert(data):
   currencies = {}
   for i in range(len(data)):
       currencies[data[i][0]] = data[i][1]
   return currencies
 

countries = convert(data)
print(countries)
