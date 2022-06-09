FROM node:14-slim as builder

WORKDIR /frontend

COPY ./package.json /frontend

RUN npm install

COPY . .

CMD [ "npm", "run", "start" ]