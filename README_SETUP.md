# 🚀 Guía de Configuración - Sistema de Gestión de Personal

## 📋 Descripción del Proyecto

Este es un sistema de gestión de personal desarrollado con **Django 5.1.7** que permite administrar información de empleados, categorías y grupos de trabajo.

## 🛠️ Requisitos del Sistema

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)
- **Bash** (para ejecutar los scripts)

## 📦 Dependencias Principales

- Django 5.1.7
- pandas 2.2.3
- numpy 2.2.4
- openpyxl 3.1.5
- psycopg2-binary 2.9.9
- gunicorn 21.2.0
- whitenoise 6.6.0

## 🚀 Instalación y Configuración

### Opción 1: Script Automatizado (Recomendado)

1. **Hacer el script ejecutable:**

   ```bash
   chmod +x setup_project.sh
   ```

2. **Ejecutar el script de configuración:**
   ```bash
   ./setup_project.sh
   ```

### Opción 2: Comandos Manuales

#### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd misApp
```

#### 2. Crear Entorno Virtual

```bash
python3 -m venv env
# En Windows:
# python -m venv env
```

#### 3. Activar Entorno Virtual

```bash
# En Linux/Mac:
source env/bin/activate

# En Windows (Git Bash):
source env/Scripts/activate

# En Windows (CMD):
env\Scripts\activate.bat
```

#### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### 5. Ejecutar Migraciones

```bash
python manage.py migrate
```

#### 6. Recopilar Archivos Estáticos

```bash
python manage.py collectstatic --no-input
```

#### 7. Ejecutar el Servidor

```bash
python manage.py runserver 8000
```

## 🌐 Acceso a la Aplicación

Una vez que el servidor esté ejecutándose, puedes acceder a la aplicación en:

- **URL Principal:** http://127.0.0.1:8000/
- **Panel de Administración:** http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
misApp/
├── gestion_personal/          # Configuración principal de Django
│   ├── settings.py           # Configuraciones del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
├── personal/                 # Aplicación de gestión de personal
│   ├── models.py            # Modelos de datos
│   ├── views.py             # Vistas de la aplicación
│   ├── forms.py             # Formularios
│   ├── templates/           # Plantillas HTML
│   └── static/              # Archivos estáticos
├── usuarios/                 # Aplicación de usuarios
│   ├── models.py            # Modelos de usuarios
│   ├── views.py             # Vistas de usuarios
│   └── templates/           # Plantillas de usuarios
├── env/                     # Entorno virtual
├── staticfiles/             # Archivos estáticos recopilados
├── manage.py                # Script de administración de Django
├── requirements.txt         # Dependencias del proyecto
└── db.sqlite3              # Base de datos SQLite
```

## 🔧 Comandos Útiles

### Script de Configuración

```bash
# Configurar todo el proyecto
./setup_project.sh

# Solo configurar el entorno
./setup_project.sh --setup

# Solo ejecutar el servidor
./setup_project.sh --run

# Mostrar ayuda
./setup_project.sh --help
```

### Comandos de Django

```bash
# Crear superusuario
python manage.py createsuperuser

# Ejecutar migraciones
python manage.py migrate

# Crear migraciones
python manage.py makemigrations

# Recopilar archivos estáticos
python manage.py collectstatic

# Ejecutar servidor en puerto específico
python manage.py runserver 8080

# Abrir shell de Django
python manage.py shell
```

## 🐛 Solución de Problemas

### Error: "Python no encontrado"

```bash
# Verificar instalación de Python
python3 --version
# o
python --version

# Si no está instalado, instalar Python desde python.org
```

### Error: "pip no encontrado"

```bash
# Instalar pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Error: "Módulo no encontrado"

```bash
# Asegurarse de que el entorno virtual esté activado
source env/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Puerto en uso"

```bash
# Usar un puerto diferente
python manage.py runserver 8080
# o
python manage.py runserver 0.0.0.0:8000
```

## 📝 Notas Importantes

1. **Entorno Virtual:** Siempre activa el entorno virtual antes de trabajar en el proyecto
2. **Base de Datos:** El proyecto usa SQLite por defecto, pero está configurado para PostgreSQL en producción
3. **Archivos Estáticos:** Los archivos estáticos se recopilan automáticamente durante el despliegue
4. **Variables de Entorno:** El proyecto usa python-dotenv para cargar variables de entorno desde un archivo .env

## 🔒 Seguridad

- No subas archivos `.env` al repositorio
- Usa contraseñas seguras para el superusuario
- En producción, configura `DEBUG = False` en settings.py

## 📞 Soporte

Si encuentras problemas durante la instalación:

1. Verifica que Python 3.8+ esté instalado
2. Asegúrate de que el entorno virtual esté activado
3. Revisa que todas las dependencias estén instaladas
4. Consulta los logs de error para más detalles

---

**¡Disfruta desarrollando con Django! 🎉**
