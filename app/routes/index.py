import logging

from fastapi import APIRouter
from sqlalchemy import select

from helpers.mysql import SessionDep, User

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/system_monitor")
async def index(db: SessionDep):
    result = await db.execute(select(User))
    user = result.scalar_one_or_none()
    print(user.name)
    return "SUCCESS"
