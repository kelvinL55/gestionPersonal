@echo off
echo ========================================
echo    INICIO RAPIDO - PROYECTO DJANGO
echo    Sistema de Gestion de Personal
echo ========================================
echo.

REM Verificar si el entorno virtual existe
if not exist "env" (
    echo Creando entorno virtual...
    python -m venv env
    echo Entorno virtual creado.
)

REM Activar entorno virtual
echo Activando entorno virtual...
call env\Scripts\activate.bat

REM Instalar dependencias si es necesario
echo Verificando dependencias...
pip install -r requirements.txt

REM Ejecutar migraciones
echo Ejecutando migraciones...
python manage.py migrate

REM Recopilar archivos estaticos
echo Recopilando archivos estaticos...
python manage.py collectstatic --no-input

REM Solicitar puerto
set /p PORT="Ingresa el puerto deseado (ejemplo: 3000, 8080, 9000) [8000]: "
if "%PORT%"=="" set PORT=8000

REM Iniciar servidor
echo.
echo ========================================
echo    INICIANDO SERVIDOR DJANGO
echo ========================================
echo.
echo Servidor iniciado en puerto %PORT%
echo Accede a: http://127.0.0.1:%PORT%/
echo.
echo Para detener el servidor presiona Ctrl+C
echo.

python manage.py runserver %PORT%

pause
