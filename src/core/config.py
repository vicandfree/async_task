import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv('PROJECT_NAME', 'ms-sales-report')

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/ms_sales_report')


