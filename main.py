from src.logger import LoggerFactory
from logging import _nameToLevel


def pyg(name: str) -> str:
    return f"pyglog logger name : '{name}' OK !"


def log(log_format=None, log_level=None) -> None:
    from os import getenv

    log_format = str(getenv("LOG_FORMAT")).upper()
    log_level = str(getenv("LOG_LEVEL")).upper()

    root = LoggerFactory.get_logger_factory().create_logger()
    root.log(level=_nameToLevel[log_level], msg=pyg(root.name))

    logger = LoggerFactory.get_logger_factory(f"{log_format}_LOGGER").create_logger()
    logger.log(level=_nameToLevel[log_level], msg=pyg(logger.name))


def pyglog() -> None:
    log()


# run pyglog
pyglog()
