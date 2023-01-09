# build stage
FROM node:lts-alpine as build-stage
WORKDIR /code
COPY package*.json ./
RUN npm install
RUN npm install -g http-server
COPY . .
CMD npm run build