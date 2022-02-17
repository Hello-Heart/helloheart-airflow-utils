"""Custom logging configuration for Apache Airflow"""

import os
from copy import deepcopy
from airflow.utils.file import mkdirs
from airflow.config_templates.airflow_local_settings import (
    DEFAULT_DAG_PARSING_LOGGING_CONFIG,
)
from airflow.config_templates.airflow_local_settings import DEFAULT_LOGGING_CONFIG


DAG_PARSING_LOGGING_CONFIG = deepcopy(DEFAULT_DAG_PARSING_LOGGING_CONFIG)
LOGGING_CONFIG = deepcopy(DEFAULT_LOGGING_CONFIG)

LOGGING_CONFIG["loggers"]["airflow.processor"]["level"] = "WARNING"
DAG_PARSING_LOGGING_CONFIG["handlers"]["processor_manager"]["maxBytes"] = (
    50 * 2**20
)  # 50MB

if os.environ.get("CONFIG_PROCESSOR_MANAGER_LOGGER") == "True":
    LOGGING_CONFIG["handlers"].update(DAG_PARSING_LOGGING_CONFIG["handlers"])
    LOGGING_CONFIG["loggers"].update(DAG_PARSING_LOGGING_CONFIG["loggers"])

    # Manually create log directory for processor_manager handler as RotatingFileHandler
    # will only create file but not the directory.
    processor_manager_handler_config = DAG_PARSING_LOGGING_CONFIG["handlers"][
        "processor_manager"
    ]
    directory = os.path.dirname(processor_manager_handler_config["filename"])
    mkdirs(directory, 0o755)
