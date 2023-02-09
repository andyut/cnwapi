import json
import requests
import pandas as pd

#data = {'temperature':'24.3'}
#data_json = json.dumps(data)

df = pd.read_csv('/data/cnwls/cnwls_obsap/update_customer.csv', delimiter=';')


CompanyDB = "LIVE_SOLO" 
UserName =  "manager"
Password = "12345"
url =  "https://192.168.6.23:50000/b1s/v1/"

mylist = df.values.tolist()

#print(mylist)

appSession = requests.Session()

#########################
# LOGIN
#########################

urllogin = url + "Login"


payload = { "CompanyDB" :CompanyDB ,
			"UserName" : UserName,
			"Password" : Password
			}
response = appSession.post(urllogin, json=payload,verify=False)

print(response.text)


#########################
# UPDATE CUSTOMER 
#########################




for line in mylist : 

	urlbp = url + "BusinessPartners('" + line[0] + "') "
   
	payload = {
				"SalesPersonCode" : line[5],
				"PayTermsGrpCode" : line[8]
			}               

	#rsp = appSession.patch(urlbp,json=payload,verify=False)
	
	print(urlbp)
	print(payload)
	#print(rsp.json())

	#apdp = rsp.json()


urllogout = url + "Logout"
#rsplogout = appSession.post(urllogout,json=payload,verify=False)




	 
# 
#response_Json = r.json() 
#print(type(json.dumps(payload)))
#print(r)
#print(response_Json)