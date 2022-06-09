FROM python:slim

WORKDIR /usr/local/bin

COPY egrid2020_data.xlsx .
COPY exp.py .

CMD [ "python", "exp.py" ]