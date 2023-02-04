from sqlalchemy import text

from db.base import database
from db.items import items
from models.item import Item, ItemTop

from .base import BaseRepository


class ItemRepository(BaseRepository):
    async def top(self) -> ItemTop:
        query = text(self.sql_raw_top())
        return await self.database.fetch_one(query=query)

    @staticmethod
    def sql_raw_top():
        return """
            select max(a.total_price) as sales_amount, a.id, a.name from 
            (select i.id, i.name, count(s.id) * i.price as total_price
            from items i
            join sales s on i.id = s.item_id 
            group by i.id) as a
            group by a.id, a.name
            order by sales_amount desc
            limit 1
         """


def get_item_repository() -> ItemRepository:
    return ItemRepository(database, model=Item, db=items)

