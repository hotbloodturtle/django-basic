FROM python:3.7.6
RUN apt-get update && apt-get -y install libpq-dev && apt-get -y install vim

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt
RUN    pip install uwsgi

ADD    ./config   /app/config/
ADD    ./manage.py   /app/

EXPOSE 80

CMD uwsgi --http "0.0.0.0:8000" --module config.wsgi --master --processes 4 --threads 2
