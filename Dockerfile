FROM python:2.7.15
COPY src /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y libpq-dev gettext
RUN pip install -r /app/requirements.txt 
WORKDIR /app/conweb
RUN python manage.py collectstatic --noinput
RUN python manage.py syncdb --noinput
RUN python manage.py migrate --noinput
RUN python manage.py compilemessages -l en
RUN python manage.py compilemessages -l zh
RUN python manage.py compilemessages -l ja
WORKDIR /app
ENTRYPOINT ["uwsgi", "--ini", "/app/uwsgi.ini"]
