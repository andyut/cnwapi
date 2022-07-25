from fastapi import APIRouter
from fastapi import Query
from app.warehouse.ItemMaster_model import ItemMaster
from typing import Optional

import json
import pymssql
import pandas as pd
import pandas.io.sql

#APIRouter creates path operations for user module
router = APIRouter(
	prefix="/Items",
	tags=["Items"],
	responses={404: {"description": "Not found"}},
)
  

@router.post("/")
async def GetItems(oitm: ItemMaster):

	host        = oitm.host
	database    = oitm.db
	user        = oitm.user
	password    = oitm.passd
	items 		= oitm.name if oitm.name else ""
	conn = pymssql.connect(host=host, user=user, password=password, database=database)        
	cursor = conn.cursor() 
	msgsql = """
					select 
							itemcode,
							itemname 
					from oitm 
					where itemname like '%""" + items + """%'
			"""


	cursor.execute(msgsql)
	rowdata = cursor.fetchall() 

	return json.dumps(rowdata, indent = 4) 