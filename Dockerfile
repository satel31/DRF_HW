FROM python:3

WORKDIR /docker_code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .