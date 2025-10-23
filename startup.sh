#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=project.settings

# Usa pasta atual se não estiver no Azure
if [ -d "/home/site/wwwroot" ]; then
    APP_ROOT="/home/site/wwwroot"
    PYTHON_CMD="python"
else
    APP_ROOT="$(pwd)"
    PYTHON_CMD="python3"  # Mac usa python3
fi

MARKER="$APP_ROOT/.fixtures_loaded"

cd "$APP_ROOT"

# Ativa ambiente virtual se estiver local (Mac)
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Executa migrações e carrega fixtures apenas uma vez
if [ ! -f "$MARKER" ]; then
    echo "Running migrations..."
    $PYTHON_CMD manage.py migrate --noinput

    echo "Loading initial data (safe mode)..."
    $PYTHON_CMD manage.py load_initial_data

    # Cria marcador para não carregar novamente
    touch "$MARKER"
fi

# Coleta arquivos estáticos
echo "Collecting static files..."
$PYTHON_CMD manage.py collectstatic --noinput || true

# Inicia o servidor Gunicorn
echo "Starting Gunicorn..."
exec gunicorn project.wsgi:application \
    --bind=0.0.0.0:8000 \
    --workers=4 \
    --timeout=600 \
    --access-logfile='-' \
    --error-logfile='-'