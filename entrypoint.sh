#!/usr/bin/env bash
mkdir -p /app/staticfiles
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn core.wsgi:application --bind 0.0.0.0:8000