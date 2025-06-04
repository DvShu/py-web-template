# py-web-template

python3 web 项目工程模板

## 包安装

推荐使用 [uv](https://docs.astral.sh/uv/) 作为包管理工具

## 依赖说明

-   开发框架: [fastapi](https://fastapi.tiangolo.com/zh/#api_2)
-   ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
-   HTTP: [httpx](https://www.python-httpx.org/)
-   ASGI: [uvicorn](https://www.uvicorn.org/)

## 运行说明

### 1. 开发环境

```bash
uv run start.py -M=development
```

开发环境下，如果未指定 `--host` 参数，则默认使用 `127.0.0.1` 作为主机地址。同时开启 `reload` 模式，以便在代码更改时自动重新加载服务器。

### 2. 生产环境

```bash
uv run start.py
```

如果未指定 `--host` 参数，则默认使用 `0.0.0.0` 作为主机地址。同时禁用 `reload` 模式

> 不管是哪种模式启动的时候都会自动加载根目录下的 `.env` 环境文件

## 日志说明

项目已经配置了日志，只需要在文件开始添加如下代码，就能进行日志记录：

```python
import logging

logger = logging.getLogger(__name__)

logger.info()
logger.exception()
```

## 项目结构

-   `start.py` - 启动文件
-   `main.py` - `Fastapi` 主文件
-   `utils` - 存放工具类
-   `scripts` - 存放辅助脚本文件
-   `routes` - 存放路由文件
-   `run` - 存放启动脚本相关的工具

## 项目脚本

1. 新建路由: `uv run scripts/cli.py [route-name]`

## 部署

复制 `.env.tmpl` 并重命名为 `.env` 然后修改配置, 启动的时候会自动加载环境配置；所以当需要在应用中读取配置时，只需要使用 `os.getenv` 即可

```bash
cp .env.tmpl .env
```

线上使用 [supervisor](https://supervisord.org/) 启动服务

## 数据库同步

项目已经集成数据库同步

1. 检查并生成更改: `uv run alembic revision --autogenerate -m "x"`
2. 执行更改: `uv run alembic upgrade head`

正确的数据库开发步骤为：

1. 修改 `helpers/mysql/models.py` 文件的表结构
2. 检查并生成更改: `uv run alembic revision --autogenerate -m "x"`
3. 执行更改: `uv run alembic upgrade head`
4. 上线的时候，执行 `uv run alembic upgrade head` 同步更改

> 切记在开发的时候，尽量不要直接操作数据库进行建库建表修改表结构等操作

## 代码检查

推荐使用 [ruff](https://docs.astral.sh/ruff/) 进行代码检查以及格式化
