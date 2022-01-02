FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY certs /code/certs
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY src /code/
ENV DJANGO_SETTINGS_MODULE letterbox.settings
EXPOSE 8000
RUN mkdir -p /var/www/django_static
RUN python manage.py collectstatic --noinput
CMD sh start.sh
