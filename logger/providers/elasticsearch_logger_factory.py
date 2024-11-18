import logging
from ecs_logging import StdlibFormatter
from .base_logger_factory import BaseLoggerFactory

class ElasticsLoggerFactory(BaseLoggerFactory):   
    
    _name: str = "ecs_logger"
    
    def __init__(self, name = _name):
        self._name = name if name else self._name
        self._formatter = StdlibFormatter()
        super().__init__(self._name)
         
    def create_logger(self) -> logging.Logger:
        from os import getenv

        self._logger.setLevel(str(getenv("LOG_LEVEL", logging.INFO)).upper())
        return self._logger
    
    def get_formatter(self) -> any:
        return self._formatter
    
    def get_format(self):
        return getattr(self.get_formatter(), '_fmt', None)