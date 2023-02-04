from datetime import datetime

import sqlalchemy

from .base import metadata

sales = sqlalchemy.Table(
    "sales",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("item_id", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('items.id'), nullable=False),
    sqlalchemy.Column("store_id", sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('stores.id'), nullable=False),
    sqlalchemy.Column("sale_time", sqlalchemy.DateTime, default=datetime.utcnow)
)
