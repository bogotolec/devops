FROM python:3.9-alpine

WORKDIR /app
RUN adduser -D user && chown -R user /app
USER user
COPY . /app

EXPOSE 8888
CMD ["python3", "server.py"]