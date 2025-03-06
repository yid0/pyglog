import os
from .providers import (
    OpenSearchLoggerFactory,
    ElasticsLoggerFactory,
    StandardLoggerFactory,
)


class LoggerFactory:
    """Factory class that creates and configures loggers based on environment settings.

    This class implements the Factory pattern to create appropriate logger instances
    based on the LOG_FORMAT environment variable.

    Available formats:
        - standard: Basic text format for console output
        - ecs: Elastic Common Schema format for ELK Stack
        - opensearch: Format optimized for OpenSearch

    Example:
        ```python
        logger = LoggerFactory.get_logger_factory("my_app").create_logger()
        logger.info("Application started")
        ```
    """

    @classmethod
    def get_logger_factory(cls, name=None):
        """Creates and returns a logger factory based on the LOG_FORMAT environment variable.

        Args:
            name (str, optional): Name for the logger instance. Defaults to None.

        Returns:
            BaseLoggerFactory: An instance of the appropriate logger factory.

        Raises:
            ValueError: If LOG_FORMAT environment variable contains an unknown format.
        """
        log_format = os.getenv("LOG_FORMAT", "standard").lower()
        match log_format:
            case "standard":
                return StandardLoggerFactory(name)
            case "ecs":
                return ElasticsLoggerFactory(name)
            case "opensearch":
                return OpenSearchLoggerFactory(name)
            case _:
                raise ValueError(f"Unknown log format: {log_format}")
