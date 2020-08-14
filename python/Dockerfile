# tiangolo/meinheld-gunicorn-flask:python3.8-alpine3.11 could be lighter on resources
# but it takes too long to build scikit-learn and scipy during iteration
FROM tiangolo/meinheld-gunicorn-flask:python3.8
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
ENV MODULE_NAME server

COPY ./src/requirements.txt /var/www/requirements.txt
COPY ./src/server.py /app
COPY ./src/model.pkl /app

RUN apt update
RUN apt -y upgrade
RUN pip install -r /var/www/requirements.txt
