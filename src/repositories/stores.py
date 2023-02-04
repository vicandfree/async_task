from sqlalchemy import text

from db.base import database
from db.stores import stores
from models.store import Store, StoreTop

from .base import BaseRepository


class StoreRepository(BaseRepository):
    async def top(self) -> StoreTop:
        query = text(self.sql_raw_top())
        return await self.database.fetch_one(query=query)

    @staticmethod
    def sql_raw_top():
        return """
            select a.id, a.address, sum(a.income_item) as income
            from (select st.id as id, st.address, count(s.item_id) * i.price as income_item
            from stores st
            join sales s on s.store_id = st.id
            join items i on s.item_id = i.id
            group by st.id, i.price) as a
            group by a.id, a.address
            order by income desc
            limit 1
         """


def get_store_repository() -> StoreRepository:
    return StoreRepository(database, model=Store, db=stores)
