@echo off
echo ========================================
echo    INICIANDO SERVIDOR DJANGO
echo ========================================
echo.

REM Solicitar puerto al usuario
set /p PORT="Ingresa el puerto deseado (ejemplo: 3000, 8080, 9000): "

REM Activar entorno virtual
call env\Scripts\activate.bat

REM Ejecutar migraciones
echo Ejecutando migraciones...
python manage.py migrate

REM Iniciar servidor en puerto personalizado
echo.
echo Iniciando servidor en puerto %PORT%...
echo Accede a: http://127.0.0.1:%PORT%/
echo.
python manage.py runserver %PORT%

pause
