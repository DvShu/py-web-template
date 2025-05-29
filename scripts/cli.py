import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="命令行创建 router 脚本参数")
    parser.add_argument("name", help="router 名称")
    args = parser.parse_args()

    main_path = Path("main.py")
    main_content = main_path.read_text(encoding="utf-8")
    main_content = main_content.replace(
        "# import router",
        f"\nfrom routes.{args.name} import router as {args.name}_router # import router\n",
    ).replace(
        "# include router",
        f'\napp.include_router({args.name}_router, prefix="/api/{args.name}")  # include router',
    )
    main_path.write_text(main_content, encoding="utf-8")

    router_path = Path(f"routes/{args.name}.py")
    router_content = [
        "import logging\n",
        "from fastapi import APIRouter\n",
        "from utils.response import json\n",
        "router = APIRouter()",
        "logger = logging.getLogger(__name__)\n",
        '@router.get("/")',
        "async def index():",
        "\treturn json()",
    ]
    router_path.write_text("\n".join(router_content), encoding="utf-8")
