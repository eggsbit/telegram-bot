FROM python:3.9.19-alpine3.20

RUN apk update
RUN apk upgrade
RUN apk add --no-cache \
    ca-certificates \
    openssl \
    curl \
    tini \
    wget \
    git

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
COPY src/main.py /app

RUN pip install -r requirements.txt

CMD ["tini", "python3", "/app/main.py"]
