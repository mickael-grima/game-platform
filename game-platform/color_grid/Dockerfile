FROM python:2.7

MAINTAINER mickaelgrima974@gmail.com

ENV PORT 8081

RUN pip install tornado

WORKDIR /workspace

COPY . .

CMD python server.py
