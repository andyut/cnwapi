from fastapi import APIRouter
import conf
from  app.common import User_router
from  app.sales import RPTSalesOrderList_router

router = APIRouter()

router.include_router(User_router.router)
router.include_router(RPTSalesOrderList_router.router)