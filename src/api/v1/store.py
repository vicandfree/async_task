from typing import List

from fastapi import APIRouter, Depends

from models.store import Store, StoreTop
from repositories.stores import StoreRepository, get_store_repository

router = APIRouter()


@router.get("/", response_model=List[Store])
async def list(stores: StoreRepository = Depends(get_store_repository)) -> List[Store]:
    return await stores.all()


@router.get("/top", response_model=StoreTop)
async def top(stores: StoreRepository = Depends(get_store_repository)) -> StoreTop:
    return await stores.top()
