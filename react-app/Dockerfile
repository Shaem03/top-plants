FROM node:14-slim as builder

WORKDIR /frontend

COPY ./package.json /frontend

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html

RUN npm install

COPY . .

EXPOSE 80

CMD [ "npm", "run", "start" ]