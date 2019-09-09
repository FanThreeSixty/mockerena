##########################
# Mockerena
# Based on ubuntu:latest
##########################
FROM ubuntu:latest

MAINTAINER Michael Holtzscher <mholtzscher@fanthreesixty.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip gunicorn3 \
    && rm -rf /var/lib/apt/lists/*

# Setup flask application
COPY . /deploy/app
WORKDIR /deploy/app
RUN pip3 install -r requirements.txt \
    && pip3 install -e .

EXPOSE 5000

# Start gunicorn
ENTRYPOINT ["/usr/bin/gunicorn3", "--config", "/deploy/app/gunicorn_config.py", "mockerena.app:app"]