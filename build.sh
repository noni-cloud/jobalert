#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
exec gunicorn jobseeker.wsgi:application --bind 0.0.0.0:${PORT:-8000}
