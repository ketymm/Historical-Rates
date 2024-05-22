# exchange API, რომელიც ბეჭდავს ლარის კურსს სასურველ ვალუტასთან მიმართებით კონკრეტულ თარიღში, რომელიც გადაეცემა input-ით

import requests
import json

key = 'hZLVv4umugm5iFeWrf0gQtmDhURJ397D'
currency = input('შეიყვანეთ ვალუტა: ').upper()
date = input("შეიყვანეთ სასურველი თარიღი აღნიშნული ფორმატით YYYY-MM-DD: ")
url = f'https://api.currencybeacon.com/v1/historical?api_key={key}&base=USD&date={date}&base={currency}'

response = requests.get(url)
# print(response)

# code = response.status_code
# print(code)

# print(response.headers)
# print(response.text)

content = response.json()

print('აღნიშნულ თარიღში კურსი გახლდათ:', content['rates']['GEL'])

file = open('exchange_rates.json', 'w')
json.dump(content, file, indent=4)
file.close()

# აღნიშნულ ბაზაში ინახება კონკრეტულ თარიღში არსებული ლარის კურსი სხვა ვალუტასთან მიმართებით
# import sqlite3
# conn = sqlite3.connect('Historical Rates')
# c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS historical_rates (
#             date DATE,
#             currency VARCHAR(10),
#             rate FLOAT)
# ''')

# c.execute("INSERT INTO historical_rates (date, currency, rate) VALUES(?, ?, ?)", (date, currency, content['rates']['GEL']))
# conn.commit()

# conn.close()