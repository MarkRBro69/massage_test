#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
uvicorn config.asgi:application --reload --host 0.0.0.0