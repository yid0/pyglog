from .base_logger_factory import BaseLoggerFactory
import logging
from ..config import load_env


class StandardLoggerFactory(BaseLoggerFactory):
    """Factory for creating standard text-format loggers.

    Creates loggers that output in a standard text format suitable for console
    and basic file logging.

    Format:
        "<timestamp> - <name> - <level> - <message>"

    Example output:
        "2024-01-15 10:30:45,123 - myapp - INFO - Application started"
    """

    _name: str = "standard_logger"

    def __init__(self, name=None):
        """Initialize the standard logger factory.

        Args:
            name (str, optional): Logger name. Defaults to 'standard_logger'.
        """
        self._name = name if name else self._name
        self._formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        super().__init__(self._name)

    def create_logger(self) -> logging.Logger:
        """Creates a configured standard logger.

        Returns:
            logging.Logger: Configured logger instance
        """
        self._logger.setLevel(load_env()["LOG_LEVEL"])
        return self._logger

    def get_formatter(self):
        return self._formatter

    def get_format(self):
        return self.get_formatter()
