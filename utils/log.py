def get_log_config():
    """获取日志配置"""
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "generic": {
                "format": "[%(asctime)s] (%(name)s) [%(levelname)s] [%(lineno)d]: %(message)s",
                "class": "logging.Formatter",
            },
        },
        "handlers": {
            "generic": {
                "formatter": "generic",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stderr",
            },
        },
        "root": {"handlers": ["generic"], "level": "INFO"},
    }
