#!/bin/bash

# Ativar ambiente virtual
source /home/site/wwwroot/antenv/bin/activate

# RESET COMPLETO - Apagar todas as tabelas
echo "========================================="
echo "Resetando banco de dados..."
echo "========================================="
python manage.py flush --noinput

# Executar migrações do zero
echo "========================================="
echo "Executando migrações..."
echo "========================================="
python manage.py migrate --noinput

# Carregar fixtures
echo "========================================="
echo "Carregando dados iniciais..."
echo "Caminho do fixture: setup/fixtures/quiz_data.json"
echo "========================================="
python manage.py loaddata setup/fixtures/quiz_data.json

if [ $? -eq 0 ]; then
    echo "✅ Fixtures carregadas com sucesso!"
else
    echo "❌ ERRO ao carregar fixtures!"
    echo "Listando arquivos de fixture:"
    ls -la setup/fixtures/
fi

# Iniciar Gunicorn
echo "========================================="
echo "Iniciando aplicação..."
echo "========================================="
gunicorn --bind=0.0.0.0:8000 --timeout 600 project.wsgi:application