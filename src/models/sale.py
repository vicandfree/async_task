from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .base import BaseModelId


class Sale(BaseModelId):
    id: Optional[int] = None
    item_id: int
    store_id: int
    sale_time: datetime


class SaleIn(BaseModel):
    item_id: int
    store_id: int


