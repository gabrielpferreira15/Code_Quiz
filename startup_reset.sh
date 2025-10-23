#!/bin/bash

# Ativar ambiente virtual
source /home/site/wwwroot/antenv/bin/activate

# RESET COMPLETO - Apagar todas as tabelas
echo "Resetando banco de dados..."
python manage.py flush --noinput

# Executar migrações do zero
echo "Executando migrações..."
python manage.py migrate --noinput

# Carregar fixtures
echo "Carregando dados iniciais..."
python manage.py loaddata setup/fixtures/quiz_data.json

# Iniciar Gunicorn
echo "Iniciando aplicação..."
gunicorn --bind=0.0.0.0:8000 --timeout 600 project.wsgi:application