from fastapi import APIRouter
from fastapi import Query
from app.sales.RPTSalesOrderList_model import  RPTSalesOrderList 

from typing import Optional

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/RPTSalesOrderList",
    tags=["RPTSalesOrderList"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def getSalesOrderList():
    return [{"id": 1}, {"id": 2}]
