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
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY ./pyproject.toml .
COPY ./poetry.lock  .

# Install poetry req global
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Project initialization:
FROM base_image

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
# RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
# COPY --chown=wagtail:wagtail ./project .

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static files.
# RUN python manage.py collectstatic --noinput --clear

CMD python manage.py migrate --noinput; gunicorn project.wsgi:application
