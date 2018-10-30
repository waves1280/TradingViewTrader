#Lists all new cryptoassets listed on Coinbase as a list.  WIP Needs to be able to list new coinbase APIs.

import requests     
import json
from apscheduler.schedulers.blocking import BlockingScheduler

##Coinbase
cb=requests.get('https://api.pro.coinbase.com/products')
cb.pairs=cb.json()
cb.list=[]
for x in range(1,len(cb.pairs)):
        cb.list.append(cb.pairs[x]['base_currency'])
cblistold=cb.list[:]
print(cblistold)
cb.newcoin=[]

def get_Coinbase_Coins():
        cb=requests.get('https://api.pro.coinbase.com/products')
        cb.pairs=cb.json()
        cb.list=[]
        cb.newcoin=[]
        cb.current=['ETH', 'BTC', 'BCH', 'LTC', 'ZRX','ETC']
        for x in range(1,len(cb.pairs)):
                cb.list.append(cb.pairs[x]['base_currency'])

        for i in range(0,len(cb.list)):
            if cb.list[i] not in cb.current:
                cb.newcoin.append(cb.list[i])
        print(list(set(cb.newcoin)))

scheduler = BlockingScheduler()
scheduler.add_job(get_Coinbase_Coins, 'interval', seconds=0.5)
scheduler.start()
