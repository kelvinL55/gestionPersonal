#!/bin/bash

echo "========================================"
echo "    INICIANDO SERVIDOR DJANGO"
echo "========================================"
echo

# Activar entorno virtual
source env/Scripts/activate

# Ejecutar migraciones
echo "Ejecutando migraciones..."
python manage.py migrate

# Iniciar servidor en puerto 8080
echo
echo "Iniciando servidor en puerto 8080..."
echo "Accede a: http://127.0.0.1:8080/"
echo
python manage.py runserver 8080
