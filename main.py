from logging import _nameToLevel

from src.pyglog import LoggerFactory
from src.pyglog.config import load_env


def pyg(name: str) -> str:
    return f"pyglog logger name : '{name}' OK !"


def log(log_format=None, log_level=None) -> None:
    log_format = load_env()["LOG_FORMAT"]
    log_level = load_env()["LOG_LEVEL"]

    root = LoggerFactory.get_logger_factory().create_logger()
    root.log(level=_nameToLevel[log_level], msg=pyg(root.name))

    logger = LoggerFactory.get_logger_factory(f"{log_format}_LOGGER").create_logger()
    logger.log(level=_nameToLevel[log_level], msg=pyg(logger.name))


def main() -> None:
    pyg("main")
    log()


if __name__ == "__main__":
    main()
