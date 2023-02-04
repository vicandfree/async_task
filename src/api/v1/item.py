from typing import List

from fastapi import APIRouter, Depends

from models.item import Item, ItemTop
from repositories.items import ItemRepository, get_item_repository

router = APIRouter()


@router.get("/", response_model=List[Item])
async def list(items: ItemRepository = Depends(get_item_repository)) -> List[Item]:
    return await items.all()


@router.get("/top", response_model=ItemTop)
async def top(items: ItemRepository = Depends(get_item_repository)) -> ItemTop:
    return await items.top()
