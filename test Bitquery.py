#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
import simplejson as json
#import json 
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
query = """query($address:String!){ethereum{address(address: {is: $address}){balances{currency{symbol, name,address}value}}}}"""
result = run_query(query)
b=json.dumps(result)
#b=("["+a+"]")
#print("b",b)
### TEST 1
b='[{"category":"DEXes","chain":"Ethereum","id":2,"name":"..............'
b=json.loads(b)
#print (b)
for row in b:
#	print(row)
        name = row["value"]["tvl"]["USD"]["value"]
        print("bbbbbbbbbbbbbbbbbbb",name)

### Test 2
c='{"originalRequest":{"category":{}},"totalResultSize":209,"products":[{"id":"1000004006560322","ean":"0828768235928","gpc":"music","title":"title","specsTag":"tag","summary":"summary","rating":45,"urls":[{"key":"DESKTOP","value":"http://www.url.com"},{"key":"MOBILE","value":"https://m.url.com"}]}]}'
c=json.loads(c)
#print ("c",c)
for row in c["products"][0]["urls"]:
#for row in b
	name = row["value"]
	print(name)



#	if name == 'WBTC':
#		WBTC = row['value']['tvl']['BTC']
#		print(WBTC)
#	symbol = row["symbol"]
#	value = str(row("value"))
#	print(token_symbol, value)
#	print(symbol)
#	print('Result - {}'.format(row["data"],["ethereum"],["address"],["balances"],["currency"],["symbol"]))
#print (result["data"]["ethereum"]["address"]["balances"]["currency"][1])
#	print ( 'Result - {}'.format(result))

#extracted_recipes = []
#for recipe in result:
#  extracted_recipes.append({
#            'symbol': recipe['currency']['symbol'],
#            'value': recipe(['balances']['value'])        })
#  print (extracted_recipes)
#  print (recipe)
import json
import pandas as pd
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
query = """query($address:String!){ethereum{address(address: {is: $address}){balances{currency{symbol, name,address}value}}}}"""
result = run_query(query)
b=json.dumps(result)
jsondata=json.loads(b)
#jsondata='''{"data":{"ethereum":{"address":[{"balances":[{"currency":{"symbol":"UNI","name":"Uniswap","address":"0x1f9840a85d5af5bf1d1762f925bdaddc4201f984","decimals":18},"value":2.288247},{"currency":{"symbol":"UNI-V2","name":"Uniswap V2","address":"0xf49c43ae0faf37217bdcb00df478cf793edd6687","decimals":18},"value":26.291958},{"currency":{"symbol":"RSR","name":"Reserve Rights","address":"0x8762db106b2c2a0bccb3a80d1ed41273552616e8","decimals":18},"value":0},{"currency":{"symbol":"UNI-V2","name":"Uniswap V2","address":"0xc5be99a02c6857f9eac67bbce58df5572498f40c","decimals":18},"value":0},{"currency":{"symbol":"ZRX","name":"0x Protocol Token","address":"0xe41d2489571d322189246dafa5ebde1f4699f498","decimals":18},"value":0},{"currency":{"symbol":"STAKE","name":"STAKE","address":"0x0ae055097c6d159879521c384f1d2123d1f195e6","decimals":18},"value":0},{"currency":{"symbol":"ETH","name":"Ether","address":"-","decimals":18},"value":0.01293373},{"currency":{"symbol":"VIDT","name":"VIDT Datalink","address":"0xfef4185594457050cc9c23980d301908fe057bb1","decimals":18},"value":506.88068},{"currency":{"symbol":"KNC","name":"Kyber Network Crystal","address":"0xdd974d5c2e2928dea5f71b9825b8b646686bd200","decimals":18},"value":0},{"currency":{"symbol":"AMPL","name":"Ampleforth","address":"0xd46ba6d942050d489dbd938a2c909a5d5039a161","decimals":9},"value":76.24007}]}]}}}'''
jsondata = jsondata[32:]
jsondata = jsondata[:-4]

df=pd.read_json(jsondata,orient='columns')
rows = []
for i,r in df.iterrows():
	rows.append({'eventid':i+1,'symbol':r['balances']['currency']['symbol'], 'name': r['balances']['currency']['name'],'value':r['balances']['value']})
df = pd.DataFrame(rows)
print(df.columns)
for i in range(len(df)) :
        qtycoin = df.loc[i,"name"]
        print(qtycoin, df.loc[i,"value"])






