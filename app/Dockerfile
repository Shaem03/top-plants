FROM python:3.8.0-slim

MAINTAINER muhammedshaheem7@gmail.com

RUN apt-get update -y

RUN apt-get install gunicorn3 -y

ENV INSTALL_PATH /app

RUN mkdir -p $INSTALL_PATH
#ADD . /usr/src/app/

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 5000

#CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:application", "--workers=5", "--timeout=300"]