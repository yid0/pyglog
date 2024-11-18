from .base_logger_factory import BaseLoggerFactory
import logging

class StandardLoggerFactory(BaseLoggerFactory):

    _name: str = "standard_logger"

    def __init__(self, name):
        self._name = name if name else self._name
        self._formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        super().__init__(self._name)

    def create_logger(self) -> logging.Logger:
        from os import getenv

        self._logger.setLevel(str(getenv("LOG_LEVEL", logging.INFO)).upper())
        return self._logger

    def get_formatter(self):
        return self._formatter

    def get_format(self):
        return self.get_formatter()