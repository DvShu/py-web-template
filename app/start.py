import argparse
import os

import uvicorn


def parse_args():
    parser = argparse.ArgumentParser(
        description="FASTAPI服务启动参数解析",
    )
    parser.add_argument(
        "-M",
        "--mode",
        help="运行环境, development、production、...",
        default="production",
        type=str,
    )
    parser.add_argument(
        "-H",
        "--host",
        help="监听地址,如果不传则根据环境自动切换0.0.0.0[production]、127.0.0.1[development]",
        type=str,
    )
    parser.add_argument(
        "-P", "--port", help="监听端口,如果不传则根据环境8000", type=int, default=8000
    )
    args = parser.parse_args()
    host = args.host
    if not host:
        host = "0.0.0.0" if args.mode == "production" else "127.0.0.1"
    args.host = host
    return args


if __name__ == "__main__":
    args = parse_args()
    os.environ["RUN_MODE"] = args.mode
    print(f"INFO:     Running in {args.mode} mode")
    uvicorn.run(
        "main:app",
        port=args.port,
        host=args.host,
        env_file=".env",
        reload=False if args.mode == "production" else True,
        access_log=False if args.mode == "production" else True,
    )
