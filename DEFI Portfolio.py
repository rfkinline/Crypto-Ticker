
#!/usr/bin/env python3
from urllib.request import urlopen
import requests
from collections import defaultdict
from json import loads

eth_token_totals = defaultdict(lambda : 0)
address ='0x9ec5e68f807b56befed7d99e9fcec6111845e7b7'
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
	gasprice = transaction.get("gasPrice")
	token_symbol = transaction.get("tokenSymbol")
	real_value = value * 10 ** (decimals * -1)
	if tx_to == address.lower():
		eth_token_totals[token_name] += real_value
	else:
		eth_token_totals[token_name] += (real_value * -1)

for token_name in eth_token_totals:
	if eth_token_totals[token_name] > 0.00001:
		print(token_name, eth_token_totals[token_name])


