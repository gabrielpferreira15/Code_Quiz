#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=project.settings

# Detecta o diretório correto (Azure usa variável de ambiente)
if [ -n "$APPSVC_VIRTUAL_ENV" ]; then
    # Azure App Service
    APP_ROOT=$(dirname "$APPSVC_VIRTUAL_ENV")
    PYTHON_CMD="python"
else
    # Local (Mac)
    APP_ROOT="$(pwd)"
    PYTHON_CMD="python3"
    # Ativa ambiente virtual se estiver local
    if [ -d ".venv" ]; then
        source .venv/bin/activate
    fi
fi

MARKER="$APP_ROOT/.fixtures_loaded"

cd "$APP_ROOT"

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