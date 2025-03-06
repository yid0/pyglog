import logging
from ecs_logging import StdlibFormatter
from .base_logger_factory import BaseLoggerFactory
from ..config import load_env


class ElasticsLoggerFactory(BaseLoggerFactory):
    """Factory for creating ECS-compatible loggers.

    Creates loggers that output in Elastic Common Schema (ECS) format,
    suitable for direct ingestion into Elasticsearch.

    Format: JSON structure following ECS specification
    Example output:
    {
        "@timestamp": "2024-01-15T10:30:45.123Z",
        "log.level": "INFO",
        "message": "Application started",
        "ecs.version": "1.0.0"
    }
    """

    _name: str = "ecs_logger"

    def __init__(self, name=_name):
        """Initialize the ECS logger factory.

        Args:
            name (str, optional): Logger name. Defaults to 'ecs_logger'.
        """
        self._name = name if name else self._name
        self._formatter = StdlibFormatter()
        super().__init__(self._name)

    def create_logger(self) -> logging.Logger:
        """Creates a configured ECS-compatible logger.

        Returns:
            logging.Logger: Configured logger instance
        """
        self._logger.setLevel(load_env()["LOG_LEVEL"])
        return self._logger

    def get_formatter(self) -> any:
        return self._formatter

    def get_format(self):
        return getattr(self.get_formatter(), "_fmt", None)
