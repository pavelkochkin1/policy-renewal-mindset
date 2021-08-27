FROM python:3.8-slim-buster

RUN mkdir /app
RUN mkdir /app/data

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["demo.py"]