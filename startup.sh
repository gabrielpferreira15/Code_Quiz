#!/bin/bash

# Ativar ambiente virtual
source /home/site/wwwroot/antenv/bin/activate

# Executar migrações
python manage.py migrate --noinput

# Iniciar Gunicorn
gunicorn --bind=0.0.0.0:8000 --timeout 600 project.wsgi:application