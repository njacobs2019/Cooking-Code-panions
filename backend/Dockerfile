FROM node:19-alpine

# Create and set working directory
RUN mkdir -p /app
RUN mkdir -p /app/public
RUN mkdir -p /app/src
WORKDIR /app

COPY package.json /app
COPY package-lock.json /app
