# https://github.com/dbt-labs/dbt-core/blob/v1.2.2/docker/Dockerfile

##
#  Generic dockerfile for dbt image building.
#  See README for operational details
##

# Top level build args
ARG build_for=linux/amd64

##
# base image (abstract)
##
FROM --platform=$build_for python:3.10.7-slim-bullseye as base

# # N.B. The refs updated automagically every release via bumpversion
# # N.B. dbt-postgres is currently found in the core codebase so a value of dbt-core@<some_version> is correct

# ARG dbt_core_ref=dbt-core@v1.2.2
# ARG dbt_postgres_ref=dbt-core@v1.2.2

# System setup
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

# Update python
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

# Install dbt via pip
RUN python -m pip install --no-cache-dir dbt-core==1.2.2 dbt-postgres==1.2.2

# dbt docs server port
EXPOSE 8080

# # Set docker basics
WORKDIR /usr/app/dbt/
VOLUME /usr/app

# ENV DBT_DIR /dbt_project
# WORKDIR $DBT_DIR

ENTRYPOINT ["dbt"]
#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]