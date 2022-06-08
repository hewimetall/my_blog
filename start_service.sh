#!/bin/sh

docker-compose -f docker-app.yml up -d
docker-compose -f docker-nginx.yml up -d
docker ps
