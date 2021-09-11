#!/bin/sh

pwd
ls

set -ex && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

cd src

python manage.py collectstatic --no-input

python manage.py makemigrations --no-input

python manage.py migrate --no-input

gunicorn school_website.wsgi -b 0.0.0.0:8000

