from fastapi import APIRouter, Depends, HTTPException, status

from models.sale import Sale, SaleIn
from repositories.sales import SaleRepository, get_sale_repository

router = APIRouter()
from dictionary import errors_dict


@router.post("/", response_model=Sale)
async def create(sale: SaleIn, sales: SaleRepository = Depends(get_sale_repository)) -> Sale:
    try:
        return await sales.create(s=sale)
    except:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errors_dict['400_sales'])
