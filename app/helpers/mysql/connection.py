from typing import Annotated, Dict, List, Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

connections = {}


def get_session(name="default"):
    """获取数据库连接

    Args:
        name (str, optional): 连接名称. Defaults to "default".

    Examples:
        async with get_session()() as session:
            result = await db.execute(select(User))
            user = result.scalar_one_or_none()

    Returns:
        async_sessionmaker: async_sessionmaker
    """
    return connections[name]["session"]


def get_session_dep(name="default"):
    """配合下面声明Depends的用法

    Args:
        name (str, optional): 连接名称. Defaults to "default".
    """

    async def session_factory():
        async with connections[name]["session"]() as session:
            yield session

    return session_factory


SessionDep = Annotated[AsyncSession, Depends(get_session_dep())]
"""这里是用于配合 fastapi.Depends 的依赖注入使用, 如果有多个连接, 就需要声明多个Dep
使用:
@router.get("/system_monitor")
async def index(db: SessionDep):
    result = await db.execute(select(User))
    user = result.scalar_one_or_none()
    print(user.name)
    return "SUCCESS"
"""


def create_connect(name: str, url_str: str):
    engine = create_async_engine(url_str, echo=True)
    session = async_sessionmaker(engine, expire_on_commit=False)
    connections["default"] = {"engine": engine, "session": session}


def connect(connection_param: Union[str, Dict[str, str], List[str]]):
    if isinstance(connection_param, str):
        create_connect("default", connection_param)
    elif isinstance(connection_param, dict):
        for name in connection_param:
            create_connect(name, connection_param[name])
    elif isinstance(connection_param, list):
        for index, value in enumerate(connection_param):
            name = f"{index}" if index > 0 else "default"
            create_connect(name, value)
    else:
        raise ValueError("connection_param must be str, dict or list")


async def dispose():
    for key in connections:
        await connections[key]["engine"].dispose()
