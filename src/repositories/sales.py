from datetime import datetime

from db.base import database
from db.sales import sales
from models.sale import Sale, SaleIn

from .base import BaseRepository


class SaleRepository(BaseRepository):
    async def create(self, s: SaleIn) -> Sale:
        sale = Sale(
            item_id=s.item_id,
            store_id=s.store_id,
            sale_time=datetime.utcnow()
        )
        values = {**sale.dict()}
        values.pop("id", None)
        query = sales.insert().values(**values)
        sale.id = await self.database.execute(query)
        return sale


def get_sale_repository() -> SaleRepository:
    return SaleRepository(database, model=Sale, db=sales)
