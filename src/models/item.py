from .base import BaseModelId


class Item(BaseModelId):
    name: str
    price: float


class ItemTop(BaseModelId):
    name: str
    sales_amount: float



