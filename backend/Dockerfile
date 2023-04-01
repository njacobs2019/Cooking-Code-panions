FROM node:19-alpine

# Expose ports (still need to expose them in compose.yaml though)
EXPOSE 3001

# Create and set working directory
RUN mkdir -p /app
RUN mkdir -p /app/src
WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm install
CMD [ "nodemon", "app.js"]