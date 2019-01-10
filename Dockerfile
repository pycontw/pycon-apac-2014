FROM python:2.7.15
COPY src /app
WORKDIR /app
RUN apt-get install -y libpq-dev
RUN ls
RUN pip install -r /app/requirements.txt 
WORKDIR /app/conweb
RUN python manage.py collectstatic --noinput
RUN python manage.py syncdb --noinput
RUN python manage.py migrate --noinput
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
