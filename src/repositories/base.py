from typing import Union

from databases import Database

from models.item import Item

MODEL_TYPE = Union[Item]


class BaseRepository:
    def __init__(self, database: Database, model: MODEL_TYPE, db):
        self.database = database
        self.model = model
        self.db = db

    async def all(self):
        query = self.db.select()
        return await self.database.fetch_all(query=query)

