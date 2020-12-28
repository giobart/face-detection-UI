FROM python:3.6-slim-buster

MAINTAINER giobart

ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5006

CMD ["gunicorn", "-c", "gunicorn_config.py", "entry:app"]

