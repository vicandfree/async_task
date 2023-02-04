import sqlalchemy

from .base import metadata

stores = sqlalchemy.Table(
    "stores",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("address", sqlalchemy.String, unique=True)
)
