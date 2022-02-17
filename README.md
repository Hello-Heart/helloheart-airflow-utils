# HelloHeart Airflow Utilities

Useful utilities for Apache Airflow, courtesy of HelloHeart.

It supports Python 3.6 - 3.8.

## Installation

### Install latest release
Latest release are uploaded to PyPi, install using pip:

```bash
pip install helloheart-airflow-utils
```

### Install from source to use latest development version
Install latest development version, clone the repository and install using Poetry:

```bash
git clone https://<helloheart-airflow-utils_repo_url>
cd helloheart-airflow-utils
poetry install
```

## Running the tests

### Single Python version testing
For testing a single Python version, use pytest (after installing from source):

```bash
pytest tests
```

### Multiple Python versions testing
For testing multiple Python versions, use tox:

```bash
tox
```