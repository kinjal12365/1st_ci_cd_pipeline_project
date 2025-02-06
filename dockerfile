FROM python:3.10-slim

COPY . /code

WORKDIR /code

EXPOSE 2000

RUN pip install -r requirements.txt 

CMD python src/app.py