FROM apache/airflow:2.4.1
USER root

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        curl

# Install dbt via pip
RUN python -m pip install --no-cache-dir dbt-core==1.2.2 dbt-postgres==1.2.2 PyYAML==6.0

USER airflow