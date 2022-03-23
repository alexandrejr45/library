FROM python:3.10-slim

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

# Install python libraries.
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy and define workdir.
COPY app/ /opt/django/app/
WORKDIR /opt/django/app/
