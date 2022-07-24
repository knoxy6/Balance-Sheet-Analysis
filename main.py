import requests
import matplotlib.pyplot as plt

api_key = open('C:/Users/cknox/Finance Projects/fmp_api_key.txt', 'r').read()

company = 'FB'
years = 2

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}/?limit={years}&apikey={api_key}')
balance_sheet = balance_sheet.json()

for i in balance_sheet[0].keys():
    print(i)

total_current_assets = balance_sheet[0]['totalCurrentAssets']
