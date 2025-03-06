from abc import ABC
import logging


class BaseLoggerFactory(ABC):
    """Abstract base class for all logger factory implementations.

    This class defines the interface that all concrete logger factories must implement.
    It handles basic logger setup including handlers and formatters.

    Attributes:
        _logger (logging.Logger): The logger instance
        _handler (logging.StreamHandler): Handler for log output
        _formatter (logging.Formatter): Formatter for log messages
    """

    _logger: logging.Logger
    _handler: logging.StreamHandler
    _formatter: logging.Formatter | None

    def __init__(self, name: str):
        """Initialize the logger factory with basic configuration.

        Args:
            name (str): Name for the logger instance
        """
        self._name = name
        self._logger = logging.getLogger(self._name)
        self._handler = logging.StreamHandler()
        self._handler.setFormatter(self._formatter)
        self._logger.addHandler(self._handler)

    @classmethod
    def create_logger(self) -> logging.Logger:
        """Creates and configures a logger instance.

        Returns:
            logging.Logger: Configured logger instance
        """
        pass

    @classmethod
    def get_formatter(self) -> logging.Formatter:
        """Returns the formatter used by this logger.

        Returns:
            logging.Formatter: The formatter instance
        """
        pass

    @classmethod
    def get_format(self) -> str:
        """Returns the format string used by the formatter.

        Returns:
            str: The format string
        """
        pass
