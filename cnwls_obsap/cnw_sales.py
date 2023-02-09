
import requests
import xlsxwriter
import numpy as np
import pandas as pd
import pandas.io.sql
import pymssql  as sapsql 

import pymssql
datacompany = (
                {'host':'192.168.250.10' , 'dbname':'IGU_LIVE','user':'sa','password':'B1admin'} ,
                )
                
datalist=[]
listcom = []
for company in datacompany:
    
    msg_sql=  """
                select  
                        'IGU' company,
                        a.docdate, 
                        substring(convert(varchar,a.docdate,112) ,5,2) imonth,
                        left(convert(varchar,a.docdate,112) ,4) iyear,
                        'Invoice' Doc,
                        a.docnum invoice,
                        a.numatcard SO,  
                        b.licTradNum NPWP,
                        a.U_IDU_FPajak FakturPajak , 
                        f.vatgroup PPn,
                        a.cardcode partnercode,
                        b.cardname partnercompany,
                        a.shiptocode partnername,
                        replace(replace(a.Address,char(13),''),char(10),'') Address,
                        replace(replace(a.Address2,char(13),''),char(10),'') Address2 , 
                        g.itemcode ,
                        g.itemname as itemname,
                        g.InvntryUom uom, 
                        f.quantity ,
                        f.price ,
                        ((f.linetotal / ( a.doctotal -a.vatsum+a.DiscSum))*a.DiscSum )  disc,
                        f.linetotal - ((f.linetotal / ( a.doctotal -a.vatsum+a.DiscSum))*a.DiscSum )  total 
                from oinv a 
                inner join ocrd b on a.cardcode = b.cardcode 
                inner join ocrg c on b.GroupCode =c.GroupCode 
                inner join oslp d on a.slpcode = d.slpcode
                inner join oslp e on b.slpcode = e.slpcode
                inner join inv1 f on a.docentry = f.docentry 
                inner join oitm g on f.itemcode = g.itemcode
                inner join OWHS h on f.whscode = h.whscode
                where a.canceled = 'N' and ( a.doctotal -a.vatsum+a.DiscSum)<>0
                and  year(a.docdate)='2021'
                union all
                select  
                        'IGU' company,
                        a.docdate, 
                        substring(convert(varchar,a.docdate,112) ,5,2) imonth,
                        left(convert(varchar,a.docdate,112) ,4) iyear,
                        'Credit Note' Doc,
                        a.docnum invoice,
                        a.numatcard SO,  
                        b.licTradNum NPWP,
                        a.U_IDU_FPajak , 
                        f.vatgroup PPn,
                        a.cardcode partnercode,
                        b.cardname partnercompany,
                        a.shiptocode partnername,
                        replace(replace(a.Address,char(13),''),char(10),'') Address,
                        replace(replace(a.Address2,char(13),''),char(10),'') Address2 , 
                        g.itemcode ,
                        g.itemname as itemname,
                        g.InvntryUom uom, 
                        -1 * f.quantity ,
                        -1 * f.price ,
                        -1 * ((f.linetotal / ( a.doctotal -a.vatsum+a.DiscSum))*a.DiscSum ) disc,
                        -1 * (f.linetotal - ((f.linetotal / ( a.doctotal -a.vatsum+a.DiscSum))*a.DiscSum ))  total 
                from orin a 
                inner join ocrd b on a.cardcode = b.cardcode 
                inner join ocrg c on b.GroupCode =c.GroupCode 
                inner join oslp d on a.slpcode = d.slpcode
                inner join oslp e on b.slpcode = e.slpcode
                inner join rin1 f on a.docentry = f.docentry 
                inner join oitm g on f.itemcode = g.itemcode
                inner join OWHS h on f.whscode = h.whscode
                where a.canceled = 'N'and ( a.doctotal -a.vatsum+a.DiscSum)<>0
                and  year(a.docdate)='2021'
                """
     
    listcom.append(company["dbname"])
    conn = sapsql.connect(host=company["host"] , user=company["user"] , password=company["password"], database=company["dbname"] )
    cursor = conn.cursor()     
    data = pandas.io.sql.read_sql(msg_sql,conn)
    datalist.append(data)

df = pd.concat(datalist)  

#df.head(5)
  
#df.to_csv("/data/.csv")
  
df.to_excel("/data/penjualan-21.xlsx")

#df.head(10).to_csv("/data/penjualantop10.csv")

 