#!/bin/bash

echo "=== Starting Code Quiz Application ==="

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Loading fixture data..."
python manage.py loaddata setup/fixtures/quiz_data.json --verbosity 2

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn server..."
gunicorn --bind=0.0.0.0:8000 --timeout 600 --workers 4 project.wsgi
