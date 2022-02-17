"""Tests for custom logging class"""

import importlib
from airflow.config_templates import airflow_local_settings
from helloheart_airflow_utils import __version__
from helloheart_airflow_utils.logging import log_config


def test_version():
    """Tests that the __version__ attribute is correct"""
    assert __version__ == "0.0.0"


def test_logging_config():
    """Tests that the LOGGING_CONFIG is not the same as airflow's default"""
    assert log_config.LOGGING_CONFIG != airflow_local_settings.DEFAULT_LOGGING_CONFIG
    log_config.LOGGING_CONFIG["loggers"]["airflow.processor"]["level"] = "INFO"
    # after reverting the change, configs are the same
    assert log_config.LOGGING_CONFIG == airflow_local_settings.DEFAULT_LOGGING_CONFIG


def test_dag_processor_logging_config():
    """
    Tests that the DAG_PARSING_LOGGING_CONFIG is not the same as airflow's default
    """
    assert (
        log_config.DAG_PARSING_LOGGING_CONFIG
        != airflow_local_settings.DEFAULT_DAG_PARSING_LOGGING_CONFIG
    )
    log_config.DAG_PARSING_LOGGING_CONFIG["handlers"]["processor_manager"][
        "maxBytes"
    ] = (100 * 2**20)
    # after reverting the change, configs are the same
    assert (
        log_config.DAG_PARSING_LOGGING_CONFIG
        == airflow_local_settings.DEFAULT_DAG_PARSING_LOGGING_CONFIG
    )


def test_complex_logging_config(monkeypatch):
    """Tests global logging config + processor_manager logging config"""
    monkeypatch.setenv("CONFIG_PROCESSOR_MANAGER_LOGGER", "True")
    importlib.reload(airflow_local_settings)
    importlib.reload(log_config)
    assert log_config.LOGGING_CONFIG != airflow_local_settings.DEFAULT_LOGGING_CONFIG
    log_config.LOGGING_CONFIG["loggers"]["airflow.processor"]["level"] = "INFO"
    log_config.LOGGING_CONFIG["handlers"]["processor_manager"]["maxBytes"] = (
        100 * 2**20
    )  # 100MB
    # after reverting the change, configs are the same
    assert log_config.LOGGING_CONFIG == airflow_local_settings.DEFAULT_LOGGING_CONFIG
