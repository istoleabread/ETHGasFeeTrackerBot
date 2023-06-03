import requests, schedule
from time import sleep
from threading import Thread

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd%2Cbtc&include_market_cap=true&include_24hr_change=true"

data = {"ethereum":{"usd":"Data Error! Please wait 15 sec:(","usd_market_cap":0,"usd_24h_change":0,"btc":0,"btc_market_cap":0,"btc_24h_change":0}}


def getdetails():
    global data
    data = requests.get(url).json()
    print(data)

schedule.every(15).seconds.do(getdetails)

def forever():
    while True:
        schedule.run_pending()
        sleep(1)

def forgwei():
    pusd = round(data['ethereum']['usd'],2)
    return pusd

t1 = Thread(target = forever)
t1.start()

def getprice():
    if type(data['ethereum']['usd']) is str:
        pusd = data['ethereum']['usd']
    else:
        pusd = round(data['ethereum']['usd'],2)
        pusd = format(pusd, ",")
    pbtc = round(data["ethereum"]["btc"], 8)
    pchange = round(data["ethereum"]["usd_24h_change"], 2)
    market = round(data["ethereum"]["usd_market_cap"])
    market = format(market, ",")
	
    price = f"""<b><ins><a href='https://coingecko.com/en/coins/ethereum/'>Ethereum | $ETH</a> Price:</ins></b>
<b>💰 USD:</b> ${pusd}
<b>🗿 BTC:</b> ฿{pbtc}
<b>📈 24h change:</b> {pchange}%
<b>💎 Market Cap:</b> ${market}
	"""
    
    return price
