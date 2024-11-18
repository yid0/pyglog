import logging
from .base_logger_factory import BaseLoggerFactory

class OpenSearchLoggerFactory(BaseLoggerFactory):
    
    _name: str ="opensearch_logger"
    
    def __init__(self, name =_name):
        self._name = name if name else self._name
        self._formatter = logging.Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')
        super().__init__(name)        
        
    def create_logger(self) -> logging.Logger:
        from os import getenv
        self._logger.setLevel(str(getenv("LOG_LEVEL", logging.INFO)).upper())
        return self._logger

    def get_formatter(self) -> logging.Formatter:
        return self._formatter    
    
    def get_format(self):
        return self.get_formatter()