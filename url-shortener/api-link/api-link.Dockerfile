FROM python:3.8.3-slim

RUN mkdir -p /home/app
WORKDIR /home/app

COPY ./api-link/requirements.txt requirements.txt
COPY ./api-link/sources .
RUN pip3 install -r requirements.txt


EXPOSE 5005

ENTRYPOINT python3 wsgi.py