FROM node:14-slim as builder

WORKDIR /frontend

COPY ./package.json /frontend

RUN npm install

COPY . .

EXPOSE 80

CMD [ "npm", "run", "start" ]