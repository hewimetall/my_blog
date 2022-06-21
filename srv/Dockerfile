# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.10-slim-bullseye AS base_image

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE $PORT

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install poetry.
RUN pip install cleo tomlkit poetry.core requests cachecontrol cachy html5lib pkginfo virtualenv lockfile poetry

COPY ./pyproject.toml .
COPY ./poetry.lock  .

# Install poetry req global
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


# Project initialization:
FROM base_image
# Use /app folder as a directory where the source code is stored.
WORKDIR /app

CMD python manage.py migrate --noinput; gunicorn project.wsgi:application
