import sqlalchemy

from .base import metadata

items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String, unique=True),
    sqlalchemy.Column("price", sqlalchemy.Float)
)
