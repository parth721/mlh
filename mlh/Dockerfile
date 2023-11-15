FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir aiohttp==3.8.5 && \
    pip install --no-cache-dir asgiref==3.7.2 && \
    # Add other packages here, installing one by one
    pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

#CMD [ "python", "manage.py", "runserver",]