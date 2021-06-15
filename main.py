import requests
import pandas as pd
from bs4 import BeautifulSoup
api_fear = 'https://api.alternative.me/fng/?limit=0&format=csv&date_format=us'
api_btc_cost = 'https://api.alternative.me/v2/ticker/bitcoin/?limit=100'

data_fear = requests.get(api_fear)
data_cost = requests.get(api_btc_cost)

# data_fear_panda = pd.read_csv(data_fear)

# print(data_fear_panda)

print(data_fear.text)
