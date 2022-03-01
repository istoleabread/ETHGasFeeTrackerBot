import requests, os
from ethprice import forgwei

API = os.environ['ether']
getgas = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey="+API
gweitoeth = 0.000000001

def gasfee():
    data = requests.get(getgas).json()

    low = int(data["result"]["SafeGasPrice"])
    avg = int(data["result"]["ProposeGasPrice"])
    fast = int(data["result"]["FastGasPrice"])
    usdp = forgwei()

    class feeusd:
        def __init__(self, usd):
            self.usd = str(round(usd * 21000 * usdp * gweitoeth, 2))
    
    lowp = feeusd(low)
    avgp = feeusd(avg)
    fastp = feeusd(fast)
    
    gasinfo = f"""<b><ins>Ethereum Live Gas Fees:</ins></b>
Low: <i>{low}</i> GWEI | <i>${lowp.usd}</i>
Average: <i>{avg}</i> GWEI | <i>${avgp.usd}</i>
High/Fast: <i>{fast}</i> GWEI | <i>${fastp.usd}</i>
    
Powered by <a href=\"etherscan.io/gastracker\">EtherScan</a>."""
    
    return gasinfo
