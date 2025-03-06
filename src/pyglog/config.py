def load_env():
    from os import getenv

    log_format = getenv("LOG_FORMAT", "standard")
    log_level = getenv("LOG_LEVEL", "info")

    return dict(
        {"LOG_FORMAT": str(log_format).upper(), "LOG_LEVEL": str(log_level).upper()}
    )
