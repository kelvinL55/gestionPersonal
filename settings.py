INSTALLED_APPS = [
    # ... existing code ...
    'usuarios',
]

LOGIN_URL = 'usuarios:login'
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'inicio'

# Si usas un modelo personalizado de usuario
AUTH_USER_MODEL = 'usuarios.Usuario' 