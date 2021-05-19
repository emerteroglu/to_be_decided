import requests
import json
import random #print(random.randrange(1, 10))
import time
#import web3.py

url = "https://api.avax.network/ext/bc/C/rpc"
c = {'Content-Type': 'application/json'}

def balance(q):
    b = json.dumps({"jsonrpc": "2.0","method": q ,"params": ["0x1409CeEe2979aD0bA18FE257c1dC789886366d25","latest"],"id": 1})
    response = requests.request("POST", url, headers=c, data=b)
    print (int(json.loads(response.text)['result'],16))

def block():
    b = json.dumps({
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 1})
    response = requests.request("POST",url, headers=c,data=b)
    return json.loads(response.text)['result']

def checktx(blc):
    #print("LATEST BLOCK: " + str(int(blc,16)))
    b = json.dumps({
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": [
        blc,
        bool(1)
    ],
    "id": 1})
    response = requests.request("POST",url,headers=c,data=b)
    #print(response.text)
    #if(response.text != None):
    response=json.loads(response.text)

    while not 'result' in response:
        time.sleep(1)
        response = requests.request("POST",url,headers=c,data=b)
        response=json.loads(response.text)
         
    dc = response['result']
    for x in dc['transactions']:
           if x['to'] == None:
                print("NEW CONTRACT DEPLOYED at block " + int(x['blockNumber'],16))

#print(type(di))#<class 'dict'>

#print(type(response)) #<class 'requests.models.Response'>

#print(type(response.text)) #<class 'str'>


#print(int(di['result'],16)) #something something

#for x in range(0,6):
 # balance("eth_getBalance")

lat = block()

while 1:
    loop=block()
    for x in range(int(lat,16),int(loop,16)):
        checktx(hex(x))
    lat=loop
