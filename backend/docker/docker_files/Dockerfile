FROM python:3.10
USER root

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN set -e && \
    apt-get update && \
    apt-get -y install netcat-traditional && \
    apt-get -y install gettext ;

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN set -e && \
    /usr/local/bin/python -m pip install --upgrade pip && \
    python -m pip install -r /code/requirements.txt 

EXPOSE 8000
CMD ["python", "manage.py", "makemigrations"]; ["python", "manage.py", "migrate"]; ["python", "manage.py", "test"]


