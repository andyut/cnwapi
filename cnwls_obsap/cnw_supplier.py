import json
import requests
import pandas as pd



df = pd.read_csv('/data/cnwls/cnwls_obsap/bp.csv', delimiter=';')

mylist = df.values.tolist()

print(mylist)

appSession = requests.Session()


# # login SAP DB
url = "https://192.168.250.36:50000/b1s/v1/Login"



payload = { "CompanyDB" :"JKUSOLOTEST" ,
			"UserName" : "manager" ,
			"Password" : "12345"
			}

response = appSession.post(url, json=payload,verify=False)

print(response.text)

# #pass parameter SAP DB
url = "https://192.168.250.36:50000/b1s/v1/BusinessPartners"

for line in mylist: 
	payload = {
			"CardCode": line[0],
			"CardName": line[1],
			"CardType": line[2] ,
			"Address" : line[3] 
			}

	response = appSession.post(url,json=payload,verify=False)

	print(response.text)



# logout SAP DB
url = "https://192.168.250.36:50000/b1s/v1/Logout"


response = appSession.post(url,verify=False)
 