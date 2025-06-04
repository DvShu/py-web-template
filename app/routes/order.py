import logging

from fastapi import APIRouter

from utils.response import json

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/create")
async def create_order():
    return json()
