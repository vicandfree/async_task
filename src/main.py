import logging

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import item, sale, store
from core import config
from core.logger import LOGGING
from db.base import database

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


app.include_router(item.router, prefix='/api/items', tags=['item'])
app.include_router(store.router, prefix='/api/stores', tags=['store'])
app.include_router(sale.router, prefix='/api/sales', tags=['sales'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=7000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
