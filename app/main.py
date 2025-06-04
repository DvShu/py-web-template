import logging.config
import os

from fastapi import FastAPI

from helpers.lifespan import lifespan
from routes.index import router as index_router
from routes.order import router as order_router  # import router
from utils.log import get_log_config

# 日志配置
logging.config.dictConfig(get_log_config())
is_prod = os.getenv("RUN_MODE", "production") == "production"
app = FastAPI(
    title="55共享",
    summary="55共享",
    description="55共享",
    version="0.0.1",
    docs_url=None if is_prod else "/docs",
    redoc_url=None if is_prod else "/redoc",
    openapi_url=None if is_prod else "/openapi.json",
    lifespan=lifespan,
)

# 注册路由
app.include_router(index_router, prefix="/api")
app.include_router(order_router, prefix="/api/order")  # include router
