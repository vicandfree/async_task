from .base import BaseModelId


class Store(BaseModelId):
    address: str


class StoreTop(BaseModelId):
    address: str
    income: float

