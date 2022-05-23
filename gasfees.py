import requests, os
from ethprice import forgwei

API = os.environ['ether'] #The etherscan.io API Key
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
            self.usd = str(round(usd * 21000 * usdp * gweitoeth, 3))
  
    lowp = feeusd(low)
    avgp = feeusd(avg)
    fastp = feeusd(fast)
    
    gasinfo = f"""<b><ins>Ethereum Live Gas Fees:</ins></b>
Low: <i>{low}</i> GWEI | ${lowp.usd}
Average: <i>{avg}</i> GWEI | ${avgp.usd}
High/Fast: <i>{fast}</i> GWEI | ${fastp.usd}
    
Powered by <a href=\"https://etherscan.io/gastracker\">EtherScan</a>"""
    
    return gasinfo



def uniswap():
    data = requests.get(getgas).json()

    low = int(data["result"]["SafeGasPrice"])
    avg = int(data["result"]["ProposeGasPrice"])
    fast = int(data["result"]["FastGasPrice"])
    usdp = forgwei()

    class uniusd:
      def __init__(self, usd):
        self.usd = str(round(usd * 184523 * usdp * gweitoeth, 3)) #184523 is the gas limit of Uniswap V3

    class univ2:
        def __init__(self, usdv2):
            self.usdv2 = str(round(usdv2 * 152809 * usdp * gweitoeth, 3)) #152809 is the gas limit of Uniswap V2

    unilow = uniusd(low)
    uniavg = uniusd(avg)
    unifast = uniusd(fast)

    unilow2 = univ2(low)
    uniavg2 = univ2(avg)
    unifast2 = univ2(fast)

    uniswapgas = f"""<b><ins>Uniswap ETH Live Gas Fees:</ins></b>
<b>V3</b>
Low: ${unilow.usd}
Average: ${uniavg.usd}
Fast: ${unifast.usd}

<b>V2</b>
Low: ${unilow2.gafe}
Average: ${uniavg2.gafe}
Fast: ${unifast2.gafe}

Powered by <a href=\"https://etherscan.io/gasTracker\">EtherScan</a>"""

    return uniswapgas
