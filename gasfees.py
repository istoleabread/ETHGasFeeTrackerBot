import requests

API = "EtherScan.io API Key"
getgas = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey="


def gasfee():
	data = requests.get(getgas + API).json()
	
	low = data["result"]["SafeGasPrice"]
	avg = data["result"]["ProposeGasPrice"]
	fast = data["result"]["FastGasPrice"]
	
	gasinfo = f"""<b><ins>Ethereum Live Gas Fees:</ins></b>
Low: <i>{low} GWEI</i>
Average: <i>{avg} GWEI</i>
High/Fast: <i>{fast} GWEI</i>
	
More info: <a href="https://etherscan.io/gasTracker">EtherScan</a>
	
Donate to support the development of this bot: /donate
	"""
	
	return gasinfo