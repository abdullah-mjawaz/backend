FROM python:3.7.4-alpine
LABEL Abullah mjawaz 


ENV PYTHONUNBUFFERED 1

COPY ./dev.requirements.txt  /dev.requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
        gcc libc-dev \
        linux-headers \
        postgresql-dev \
        libffi \ 
        libffi-dev
 
RUN apk --update add \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev \
    build-base \
    jpeg-dev \
    zlib-dev
RUN apk --update add fontconfig font-noto
RUN pip install --upgrade pip
RUN pip install -r /dev.requirements.txt

RUN apk del .temp-build-deps 

RUN mkdir /app
WORKDIR /app
COPY . /app
# RUN adduser -D user
USER root