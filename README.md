# **Pyglog: Python Generic Logger**

**Pyglog** is a versatile and modular logging solution for Python applications, designed to meet modern logging needs with flexibility and efficiency. It enables developers to generate logs in specific, customizable formats, ensuring seamless integration with powerful tools such as **ELK Stack**, **OpenSearch**, and other log aggregation systems.

## **Installation**

### Using pip
```bash
pip install pyglog
```

### From source
```bash
git clone https://github.com/yid0/pyglog.git
cd pyglog
pip install -r requirements.txt
```

## **Quick Start**

1. Set up environment variables (required):
```bash
export LOG_FORMAT="standard"  # Available formats: standard, ecs, opensearch
export LOG_LEVEL="INFO"      # Available levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

2. Use in your Python code:
```python
from pyglog import LoggerFactory

# Get a logger instance
logger = LoggerFactory.get_logger_factory("MY_LOGGER").create_logger()

# Log messages
logger.info("This is an info message")
logger.error("This is an error message")
```

3. Run the example script:
```bash
python main.py
```

## **Using Make Commands**

You can use make commands to quickly test different logging configurations:

```bash
# Format: make log-{LOG_LEVEL}-{LOG_FORMAT}

# Standard format examples
make log-info-standard    # INFO level with standard format
make log-error-standard   # ERROR level with standard format

# ECS format examples
make log-info-ecs        # INFO level with ECS format
make log-fatal-ecs       # FATAL level with ECS format

# OpenSearch format examples
make log-error-ops       # ERROR level with OpenSearch format

# Multiple formats at once
make log-info           # Runs both standard and ECS formats with INFO level
```

Available combinations:
- LOG_LEVEL: info, error, fatal
- LOG_FORMAT: standard, ecs, ops (shorthand for opensearch)

## **Key Features**
- **Customizable Formats**: Define log formats to suit the needs of various systems and workflows.
- **Ease of Integration**: Optimized for seamless injection into ELK Stack, OpenSearch, and similar platforms.
- **Singleton Pattern**: Ensures a single logger instance per application or component, reducing configuration redundancy.
- **Dynamic Configuration**: Adapt logging levels and formats dynamically through environment variables or runtime settings.
- **Thread-Safe Design**: Reliable in multithreaded environments, ensuring consistent logging without conflicts.
- **Extensibility**: Ready for integration with additional backends or custom log handlers.


| **Feature**                               | **Implemented in Pyglog?**                              | **Comments**                                                                            |
|-------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Customizable Formats**                  | Yes                                                     | Formats can be defined using a `Formatter`.                                            |
| **Ease of Integration (ELK, OpenSearch)** | Yes (partially)                                         | Logs can be formatted for these tools, but direct integration via API could be added.  |
| **Singleton Pattern**                     | Yes (via the Factory, if used)                         | The Factory ensures a single instance per name, corresponding to a targeted Singleton. |
| **Dynamic Configuration**                 | Yes                                                     | Logging levels and formats can be dynamically configured via environment variables.    |
| **Thread-Safe Design**                    | Yes                                                     | Python's `logging` module is natively thread-safe.                                     |
| **Extensibility**                         | No                                                     | Supports additional handlers like `StreamHandler`, `FileHandler`, etc.                |

## **Use Cases**
- Centralized logging in **microservices architectures**.
- Debugging and monitoring **distributed systems**.
- Real-time log analysis and visualization with **ELK** or **OpenSearch**.
- Flexible logging for **cloud-native applications**, including **Kubernetes deployments**.

## **Configuration Options**

### Environment Variables
- `LOG_FORMAT`: Define the output format (standard, ecs, opensearch)
  - `standard`: Basic text format suitable for console output and basic logging
  - `ecs`: Format compatible with Elastic Common Schema for ELK Stack integration
  - `opensearch`: Format optimized for OpenSearch data ingestion
- `LOG_LEVEL`: Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Available Log Formats
1. Standard Format:
```
2024-11-15 10:30:45,123 - MY_LOGGER - INFO - Your log message
```

2. ECS Format:
```json
{
    "@timestamp": "2024-11-15T10:30:45.123Z",
    "log.level": "INFO",
    "logger.name": "MY_LOGGER",
    "message": "Your log message",
    "ecs.version": "1.0.0"
}
```

3. OpenSearch Format:
```json
{
    "timestamp": "2024-11-15T10:30:45.123Z",
    "severity": "INFO",
    "logger": "MY_LOGGER",
    "message": "Your log message",
    "metadata": {
        "format": "opensearch"
    }
}
```


## License 📄
MIT License

## Author 👨‍💻
[Yani IDOUGHI](https://www.linkedin.com/in/yid0/)