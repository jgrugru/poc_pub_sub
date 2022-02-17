FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN pip3 install poetry

COPY . .


RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
