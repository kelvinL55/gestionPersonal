#!/usr/bin/env bash
# Script para construir y preparar la aplicación para su despliegue en Render

set -o errexit  # Salir inmediatamente si un comando falla

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate 