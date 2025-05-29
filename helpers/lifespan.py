import logging
import os
from contextlib import asynccontextmanager

from helpers.mysql import connect, dispose

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app):
    connect(os.getenv("MYSQL_URL"))
    yield
    await dispose()
