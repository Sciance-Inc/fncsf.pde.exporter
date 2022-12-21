FROM python:3.8

RUN apt-get update && apt-get upgrade -y

RUN pip install poetry

COPY . /app

WORKDIR /app

RUN poetry install

CMD poetry run pde_fncsf_exporter export .