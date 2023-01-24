FROM python:3.10-slim as python-base

# Upgrade system.
RUN apt-get -y update
RUN apt-get -y upgrade

# Install required programs.
RUN apt-get -y install nano \
                       locales \
                       vim \
                       libpq-dev

RUN apt-get install ca-certificates

# Set locale and python environment variables.
RUN locale-gen pt_BR.UTF-8
RUN localedef -c -i pt_BR -f UTF-8 pt_BR.UTF-8
RUN update-locale LANG=pt_BR.UTF-8

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt
ENV LC_ALL pt_BR.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache

# Creating a virtual environment just for poetry and install it with pip
RUN pip3 install -U pip setuptools \
    && pip3 install poetry==${POETRY_VERSION}

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
# Copy Dependencies
COPY poetry.lock pyproject.toml ./

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

RUN poetry config virtualenvs.create false
# Install Dependencies
RUN poetry install --no-interaction --no-cache --without dev

# Copy Application

COPY . /app


