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


val = ast.literal_eval(mystr)
df=[]
val1 = json.loads(json.dumps(val))
val2 = val1['address'][0]['balances']
df= pd.DataFrame(val2, columns=['value'])
print(df)
val2 = val1['address'][0]['balances'][0]['currency']['sym$

#print (pd.DataFrame(val2.items()))
#df=pd.DataFrame(val2,columns=['symbol','name'])
df.append(val2, ignore_index=True)
print (df)









