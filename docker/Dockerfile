FROM python:3.8

RUN mkdir /upload

RUN chmod -R 444 /upload

RUN apt-get update && apt-get upgrade -y

RUN pip install poetry

ADD . /app

WORKDIR /app

RUN poetry install

CMD poetry run pde_fncsf_exporter export /upload