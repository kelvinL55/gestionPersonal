"""
Configuración específica para Render con PostgreSQL
Copia este contenido a settings.py si el problema persiste
"""

# Configuración de base de datos específica para Render
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    # Configuración más permisiva para Render
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', ''),
            'USER': os.environ.get('DB_USER', ''),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', ''),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'prefer',  # Preferir SSL pero no requerirlo
                'connect_timeout': 10,
            },
        }
    }
else:
    # Fallback a SQLite para desarrollo local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
