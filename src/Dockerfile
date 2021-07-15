FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8

COPY    ./requirements.txt ./
RUN     pip install -r requirements.txt

COPY    ./ src/
WORKDIR src/

CMD     python -u main.py