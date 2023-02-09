
import xlsxwriter
import numpy as np
import pandas as pd
import pandas.io.sql
import pymssql   

import pymssql
datacompany = (
                {'host':'192.168.250.10' , 'dbname':'IGU_LIVE','user':'sa','password':'B1admin'} ,
                )
                
datalist=[]
listcom = []
for company in datacompany:
    
    msg_sql=  """
select
        A.ItemCode ,
        A.ItemName ,
        A.ItemType ,
        A.SellItem ,
        A.InvntItem ,
        A.PrchseItem ,
        A.AssetItem ,
        A.U_Group ,
        a.U_SpeGroup ,
        a.U_SubGroup ,
        a.U_Brand ,
        a.U_Category,
        a.U_Country ,
        a.U_Cutting,
        a.U_HS_Code ,
        A.U_Old_Code ,
        a.U_Grading ,
        a.InvntryUom ,
        a.VatGourpSa ,
        a.VatGroupPu,
        a.ItmsGrpCod  
        

from OITM A 
WHERE InvntItem='Y'

                """
     
    listcom.append(company["dbname"])
    conn = pymssql.connect(host=company["host"] , user=company["user"] , password=company["password"], database=company["dbname"] )
    cursor = conn.cursor()     
    data = pandas.io.sql.read_sql(msg_sql,conn)
    datalist.append(data)

df = pd.concat(datalist)  

listvalue = df.values.tolist()
for line in listvalue:
        print(line[2])
#df.to_csv("/data/.csv")
  
#df.to_excel("/data/penjualan-21.xlsx")

#df.head(10).to_csv("/data/penjualantop10.csv")

 

 