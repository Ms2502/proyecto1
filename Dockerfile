FROM alpine:3.16

WORKDIR /home/f1/

COPY . /home/f1/

RUN apk add py3-pip

RUN python3 /home/f1/oneto100.py

