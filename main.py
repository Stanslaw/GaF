import json
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

api_fear = 'https://api.alternative.me/fng/?limit=0&date_format=us'
api_btc_cost = 'https://api.alternative.me/v2/ticker/bitcoin/?limit=100'

data_fear = requests.get(api_fear)
data_cost = requests.get(api_btc_cost)

data_json = json.loads(data_fear.text)

data_fear_panda = pd.DataFrame(data_json['data'])

#Делаем дату датой
data_fear_panda.timestamp = pd.to_datetime(data_fear_panda.timestamp)

#Делаем Числа числами
data_fear_panda.value = pd.to_numeric(data_fear_panda.value)

graph = data_fear_panda[['timestamp', 'value', 'value_classification']]

print(graph)

ax1 = graph.plot(x='timestamp', y='value', grid=True)

plt.show()
