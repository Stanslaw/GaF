import json
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

api_fear = 'https://api.alternative.me/fng/?limit=0&date_format=us'
api_btc_cost = 'https://api.alternative.me/v2/ticker/bitcoin/?limit=100'

data_fear = requests.get(api_fear)
data_cost = requests.get(api_btc_cost)

data_json = json.loads(data_fear.text)

data_fear_panda = pd.DataFrame(data_json['data'])

#Делаем дату датой
data_fear_panda.timestamp = list(map(lambda x: datetime.strptime(x, '%m-%d-%Y'), data_fear_panda.timestamp))

data_fear_panda.reindex(index=data_fear_panda.timestamp)

print(data_fear_panda)

# graph = data_fear_panda[['timestamp', 'value']]
#
# graph.plot()

# plt.show()
