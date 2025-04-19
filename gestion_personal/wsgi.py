"""
Configuración WSGI para el proyecto gestion_personal.
Este archivo expone la aplicación WSGI como una variable de módulo llamada 'application'.
Carga automáticamente las variables de entorno desde un archivo .env para facilitar la configuración en producción y desarrollo.
"""
import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_personal.settings')

application = get_wsgi_application()

