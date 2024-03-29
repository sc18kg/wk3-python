import requests
from bs4 import BeautifulSoup

url = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
content = requests.get(url).content
html = BeautifulSoup(content, 'html.parser')
#print(html.prettify())

forex_table = html.find('table', {'class': 'forextable'})
#print(forex_table)

table_body = forex_table.find('tbody')
#print(table_body)

table_rows = table_body.find_all('tr')
#print(table_rows)

forex_dict = {}
for row in table_rows:
    for td in row.find_all('td'):
        if td.has_attr('id'):
            currency = td.find('a').text
        elif td.a.find('span'):
            rate = td.a.find('span').text
    forex_dict[currency] = rate

print(forex_dict)