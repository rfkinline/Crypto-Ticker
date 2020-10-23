
#!/usr/bin/env python3
from urllib.request import urlopen
import requests
from collections import defaultdict
from json import loads

eth_token_totals = defaultdict(lambda : 0)
#address ='0x9ec5e68f807b56befed7d99e9fcec6111845e7b7'
address='0x03F2C52f1Cd2043AF5AD4B9C16B689B2B28bD8Ac'

url = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(url)
pricejson = response.json()


url = 'https://api.etherscan.io/api?module=account&action=tokentx&address='+address+'&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
response = requests.get(url)
address_content = response.json()
result = address_content.get("result")
for transaction in result:
	tx_from = transaction.get("from")
	tx_to = transaction.get("to")
	value = int(transaction.get("value"))
	decimals = int(transaction.get("tokenDecimal"))
	token_name = transaction.get("tokenName")
	token_symbol = transaction.get("tokenSymbol")
	gasprice = int(transaction.get("gasPrice"))
	gasused = int(transaction.get("gasUsed"))
	gasprice=gasused/1000000000*gasprice/1000000000
	real_value = value * 10 ** (decimals * -1)
	if tx_to == address.lower():
		eth_token_totals[token_symbol] += real_value
		gasprice+=gasprice
	else:
		eth_token_totals[token_symbol] += (real_value * -1)
		gasprice+=gasprice
#	symbol=DAI name=Dai Stablecoin
#'id': 'zulu-republic-token', 'symbol': 'ztx', 'name': 'Zulu Republic Token'
	print(token_name, gasprice)
for token_symbol in eth_token_totals:
	if eth_token_totals[token_symbol] > 0.00001:
		pricetoken=0
		symbol_lower = token_symbol.lower()
		for token in pricejson:
			if token['symbol'].lower() == symbol_lower:
#					pricetoken = float(loads(urlopen('https://min-api.cryptocompare.com/data/price?fsym='+ symbol_lower +'&tsyms=BTC,USD,EU').read())['USD'])
				pricetokenunit = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/' + token['id']).read())['market_data']['current_price']['usd'])

# not allways 100%, For example BLZ and contract 0x62450755160E9347DcF947da31AcC841E9668443 Iscariot (BLZ). Price should be 0
				
		pricetoken=pricetokenunit*eth_token_totals[token_symbol]
		currency = "${:,.2f}".format(pricetoken)
		print(token_symbol,eth_token_totals[token_symbol], currency)


	#	[{"blockNumber":"10451980",
	#	"timeStamp":"1594653491",
	#	"hash":"0x2b72e1e454ef895ddee5da46ec2a154a7460692d316fe87d15e2fab7bb1e4070",
	#	"nonce":"0",
	#	"blockHash":"0x1b28b88e744ffec253b91d68066295b7a1c9adb9b8046f22b027b06acb0184ae",
	#	"from":"0x03f2c52f1cd2043af5ad4b9c16b689b2b28bd8ac",
	#	"contractAddress":"0x0000000000004946c0e9f43f4dee607b0ef1fa1c",
	#	"to":"0x0000000000000000000000000000000000000000",
	#	"value":"0",
	#	"tokenName":"Chi Gastoken by 1inch",
	#	"tokenSymbol":"CHI",
	#	"tokenDecimal":"0",
	#	"transactionIndex":"148",
	#	"gas":"659066",
	#	"gasPrice":"73650000000",
	#	"gasUsed":"402508",
	#	"cumulativeGasUsed":"9759222",
	#	"input":"deprecated",
	#	"confirmations":"655728"},
	#	print(transaction.get("gas"),transaction.get("gasPrice"),transaction.get("gasUsed"),transaction.get("cumulativeGasUsed"),transaction.get("timeStamp"), "R")
