#!/usr/bin/env bash
# exit on error
set -o errexit

pip install dj-database-url django djangorestframework whitenoise psycopg2-binary coreapi gunicorn

python manage.py collectstatic --no-input
python manage.py migrate