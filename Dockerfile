FROM python:3.6-alpine

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install "connexion[swagger-ui]"

COPY . /app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
