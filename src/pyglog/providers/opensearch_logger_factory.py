import logging
from .base_logger_factory import BaseLoggerFactory
from ..config import load_env


class OpenSearchLoggerFactory(BaseLoggerFactory):
    """Factory for creating OpenSearch-compatible loggers.

    Creates loggers that output in a format optimized for OpenSearch ingestion.
    The output format is JSON-structured with fields specific to OpenSearch.

    Format: JSON structure with OpenSearch-specific fields
    Example output:
    {
        "timestamp": "2024-01-15T10:30:45.123Z",
        "level": "INFO",
        "message": "Application started"
    }
    """

    _name: str = "opensearch_logger"

    def __init__(self, name=_name):
        """Initialize the OpenSearch logger factory.

        Args:
            name (str, optional): Logger name. Defaults to 'opensearch_logger'.
        """
        self._name = name if name else self._name
        self._formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
        )
        super().__init__(name)

    def create_logger(self) -> logging.Logger:
        """Creates a configured OpenSearch-compatible logger.

        Returns:
            logging.Logger: Configured logger instance
        """
        self._logger.setLevel(load_env()["LOG_LEVEL"])
        return self._logger

    def get_formatter(self) -> logging.Formatter:
        return self._formatter

    def get_format(self):
        return self.get_formatter()
