FROM apache/airflow:2.4.1
USER root

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        curl

USER airflow