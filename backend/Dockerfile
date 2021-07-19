FROM    python:3.6.13-slim-buster

ARG     DEBIAN_FRONTEND=noninteractive

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
ENV     FLASK_APP=app.py FLASK_RUN_PORT=7777

COPY    ./requirements.txt ./
RUN     pip install -r requirements.txt

COPY    ./ src/
WORKDIR src/

CMD     gunicorn --bind 0.0.0.0:7777 -k gevent --worker-connections 1000 \
        --access-logfile '-' --error-logfile '-' --capture-output server:app