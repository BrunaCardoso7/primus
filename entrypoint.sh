#!/usr/bin/env bash

set -e

mkdir -p /app/staticfiles

python manage.py collectstatic --noinput
python manage.py migrate --noinput

exec gunicorn core.wsgi:application --bind 0.0.0.0:8000