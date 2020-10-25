
#!/usr/bin/env python3
from urllib.request import urlopen
import requests
from json import loads
import pandas as pd

#address ='0x9ec5e68f807b56befed7d99e9fcec6111845e7b7'
address='0x82eaa009e9cae43955a3ef9d1de3bf68f5154200'

df = pd.DataFrame() 
#ValueError: invalid literal for int() with base 10: 'Max rate limit reached, please use API Key for higher rate limit'

url = 'https://api.etherscan.io/api?module=account&action=tokentx&address='+address+'&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken'
response = requests.get(url)
status = requests.get(url).status_code
if status == 200:
	address_content = response.json()
	result = address_content.get("result")
	for transaction in result:
		tx_from = transaction.get("from")
		tx_to = transaction.get("to")
		contractAddress = transaction.get("contractAddress")
		value = int(transaction.get("value"))
		decimals = int(transaction.get("tokenDecimal"))
		token_name = transaction.get("tokenName")
		token_symbol = transaction.get("tokenSymbol")
		gasprice = int(transaction.get("gasPrice"))
		gasused = int(transaction.get("gasUsed"))
		gasfee=gasused/1000000000*gasprice/1000000000
		real_value = value * 10 ** (decimals * -1)
		if tx_to == address.lower():
			real_value = real_value
		else:
			real_value = (real_value * -1)
		df = df.append({'contractAddress':contractAddress, 'token_symbol':token_symbol, 'real_value':real_value}, ignore_index=True)

url = 'https://api.etherscan.io/api?module=account&action=balance&address='+address+'&tag=latest&apikey=YourApiKeyToken'
response = requests.get(url).json()
status = requests.get(url).status_code
if status == 200:
	value = int(response['result'])
	contractAddress = address
	token_name = "Ethereum"
	token_symbol = "ETH"
	real_value = value / 1000000000000000000
	df = df.append({'contractAddress':contractAddress, 'token_symbol':token_symbol, 'real_value':real_value}, ignore_index=True)

df=df.groupby(['token_symbol','contractAddress'],as_index=False).agg(sum)

#problem tokens: AMPL 
#HEX2T and SoftLink no price in etherscan

for i in range(len(df)) :
	if df.loc[i,"real_value"] > 0.00001:
		pricetokenunit=0
		try:
			pricetokenunit = float(loads(urlopen('https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=' + df.loc[i,"contractAddress"] +'&vs_currencies=usd').read())[df.loc[i,"contractAddress"]]['usd'])
		except:
			pricetokenunit=0
		if df.loc[i,"contractAddress"] == address:
			pricetokenunit = float(loads(urlopen('https://api.coingecko.com/api/v3/coins/ethereum').read())['market_data']['current_price']['usd'])
		pricetoken=pricetokenunit * df.loc[i,"real_value"]
		currency = "${:,.2f}".format(pricetoken)
		print(df.loc[i,"token_symbol"],df.loc[i,"real_value"], currency)


#'id': 'zulu-republic-token', 'symbol': 'ztx', 'name': 'Zulu Republic Token'
#	print(df.loc[i,"contractAddress"])
	#	"blockNumber":"10451980",
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