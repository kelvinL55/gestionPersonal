@echo off
echo ========================================
echo    INICIANDO SERVIDOR DJANGO
echo ========================================
echo.

REM Activar entorno virtual
call env\Scripts\activate.bat

REM Ejecutar migraciones
echo Ejecutando migraciones...
python manage.py migrate

REM Iniciar servidor en puerto 8080
echo.
echo Iniciando servidor en puerto 8080...
echo Accede a: http://127.0.0.1:8080/
echo.
python manage.py runserver 8080

pause
