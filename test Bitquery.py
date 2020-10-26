#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
address='0x8998aC6F6d538207015F11E0aCfE7300FBa350E1'

def run_query(query):  # A simple function to use request$
	global address
	print(address)
	request = requests.post('https://graphql.bitquery.io/',	json = {"query":query, "variables":{"address": address}})
	if request.status_code == 200:
		return request.json()
	else:
		raise Exception('Query failed and return code is {}.{}'.format(request.status_code,query))
query = """query($address:String!){ethereum{address(address: {is: $address}){balances{currency{symbol, name,address}}value}}}}"""
result = run_query(query)  # Execute the query
for transaction in result:
#	token_symbol = transaction.get("tokenSymbol")
#	value = int(transaction.get("value"))
#	print(token_symbol, value)
#	print 'Result - {}'.format(result)

 ["data"],["ethereum"],["address"],["balances"],["currency"],["symbol"]