from .base import engine, metadata
from .items import items
from .sales import sales
from .stores import stores

metadata.create_all(bind=engine)
