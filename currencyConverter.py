''''
Notes for self:
    1. Skills used: Python Dictionaries, Input/Output, typecasting, recurssion, beautifulsoup, html parsing
'''

''''
    Starting Phase:
        1. Welcome message
        2. List of countries

'''

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
       currencies[i+1] = {data[i][0] : data[i][1]}
   currencies[len(currencies)] = {"U.S. Dollar" : 1}
   return currencies
 


print("\nWelcome to Currency Converter!")
print("We have over 50 currencies available to convert\n")

countries = convert(data)
             

# Printing all currency options
for key, value in countries.items():
    for currency, rate in value.items():
        print(str(key) + " : " + currency)
print("\n")

# Part 1 Starting Currency 
#Takes input from user and assigns starting_currency variable based on input
def choosingStartingCurrency(): 
    initial_currency_key = int(input("Enter the number associated with your starting currency: "))
    starting_currency = countries.get(initial_currency_key, None) # stores dict value
    if (starting_currency == None): # Will run until a valid currency is assigned to starting_currency
        print("\nYou entered the wrong number. Please use a number associated with a currency.")
        starting_currency = choosingStartingCurrency()
    return starting_currency

starting_currency = choosingStartingCurrency() # returns a dict with currency:rate pair
starting_currency_name = [key for key in starting_currency.keys()][0] # Access the key in the first item of dictionary i.e. currency name
starting_currency_exchange_rate = [value for value in starting_currency.values()][0] # Access the value in the first item of dictionary i.e. exchange rate



# Part 2 Amount
starting_amount = float(input("Enter the amount of " + starting_currency_name + " : "))

while(starting_amount < 0): #Runs until starting_amount is assigned a non-negative value
    print("\nInvalid Input!  Please enter an amount greater than or equal to zero")
    starting_amount = int(input("Enter the amount of " + starting_currency_name + " : "))



# Part3 Required currency 
print("\n")
for key, value in countries.items():
    for currency, rate in value.items():
        if(starting_currency_name == currency): #skips initial_currency_key 
            continue
        print(str(key) + " : " + currency)
print("\n")

# Choosing Final Currency
def choosingFinalCurrency(): #Takes input from user and assigns final_currency variable based on input
    final_currency_key = int(input("Enter the number associated with your final currency: "))
    final_currency =  countries.get(final_currency_key, None)

    if (final_currency == starting_currency):
        final_currency = None

    if (final_currency == None): # Will run until a valid currency is assigned to final_currency
        print("\nYou entered the wrong number. Please use a number associated with a currency.")
        final_currency = choosingFinalCurrency()
    return final_currency

final_currency = choosingFinalCurrency()
final_currency_name = [key for key in final_currency.keys()][0]
final_currency_exhange_rate = [value for value in final_currency.values()][0]


#At this point you have:
# starting_currency_name, final_currency_name, exchange rate1, exchnage rate 2, starting amount
# We convert the value of starting amount to final amount

amount_in_dollars = starting_amount / float(starting_currency_exchange_rate)
final_amount = amount_in_dollars * float(final_currency_exhange_rate)

print(str(starting_amount) + " " + str(starting_currency_name) + " in " + str(final_currency_name) + " = " + str(round(final_amount, ndigits=2)))