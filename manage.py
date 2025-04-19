"""
Archivo principal para la gestión de comandos administrativos de Django.
Carga automáticamente las variables de entorno desde un archivo .env para facilitar la configuración en desarrollo y producción.
"""
import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def main():
    """
    Ejecuta las tareas administrativas de Django.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_personal.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
