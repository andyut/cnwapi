from pydantic import BaseModel, Field
from typing import Optional

from pyrsistent import s

class ItemMaster(BaseModel):
    name  : str = "a"
    host  : str = "192.168.250.36"
    db    : str = "IGU_LIVE"
    user  : str = "sa"
    passd : str = "B1admin"