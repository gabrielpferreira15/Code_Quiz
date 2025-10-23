#!/bin/bash

# Detectar o diretório correto da aplicação
if [ -d "/tmp/8de11e555e54126" ]; then
    APP_PATH="/tmp/8de11e555e54126"
elif [ -d "/home/site/wwwroot" ]; then
    APP_PATH="/home/site/wwwroot"
else
    APP_PATH="."
fi

cd $APP_PATH

echo "========================================="
echo "Diretório da aplicação: $APP_PATH"
echo "========================================="

# Ativar ambiente virtual
source $APP_PATH/antenv/bin/activate

# Executar migrações
echo "Executando migrações..."
python manage.py migrate --noinput

# Iniciar Gunicorn
echo "Iniciando aplicação..."
gunicorn --bind=0.0.0.0:8000 --timeout 600 project.wsgi:application