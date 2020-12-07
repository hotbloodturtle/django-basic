FROM python:3.7.6

ENV PYTHONUNBUFFERED 0

RUN apt-get update && apt-get -y install libpq-dev && apt-get -y install vim

# zsh
RUN apt-get install -y zsh
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN chsh -s /usr/bin/zsh

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

ADD . .

RUN    pip install -r requirements.txt

CMD python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    uwsgi --socket :8000 \
          --wsgi config.wsgi \
          --processes 4 \
          --threads 2 \
          --lazy-apps \
          --buffer-size 32768

