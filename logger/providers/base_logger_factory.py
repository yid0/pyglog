from abc import ABC
import logging

class BaseLoggerFactory(ABC):
    _logger: logging.Logger
    _handler: logging.StreamHandler
    _formatter: logging.Formatter | None
    
    def __init__(self, name: str):
        self._name = name
        self._logger = logging.getLogger(self._name)
        self._handler = logging.StreamHandler()
        self._handler.setFormatter(self._formatter)
        self._logger.addHandler(self._handler)

    @classmethod
    def create_logger(self) -> logging.Logger:
        pass
    
    @classmethod
    def get_formatter(self) -> logging.Formatter :
        pass
    
    @classmethod
    def get_format(self) -> str :
        pass
