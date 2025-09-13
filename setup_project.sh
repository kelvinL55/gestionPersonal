#!/bin/bash

# ========================================
#    SCRIPT DE CONFIGURACIÓN DEL PROYECTO
#    Sistema de Gestión de Personal - Django
# ========================================

echo "========================================"
echo "   CONFIGURANDO PROYECTO DJANGO"
echo "   Sistema de Gestión de Personal"
echo "========================================"
echo ""

# Función para mostrar ayuda
mostrar_ayuda() {
    echo "Uso: $0 [OPCIÓN]"
    echo ""
    echo "Opciones:"
    echo "  -h, --help     Mostrar esta ayuda"
    echo "  -c, --clone    Solo clonar el repositorio"
    echo "  -s, --setup    Solo configurar el entorno"
    echo "  -r, --run      Solo ejecutar el servidor"
    echo "  -a, --all      Ejecutar todo el proceso (por defecto)"
    echo ""
    echo "Ejemplos:"
    echo "  $0                    # Configurar y ejecutar todo"
    echo "  $0 --clone            # Solo clonar"
    echo "  $0 --setup            # Solo configurar entorno"
    echo "  $0 --run              # Solo ejecutar servidor"
}

# Función para verificar si Python está instalado
verificar_python() {
    echo "Verificando instalación de Python..."
    if command -v python3 &> /dev/null; then
        echo "✓ Python3 encontrado: $(python3 --version)"
    elif command -v python &> /dev/null; then
        echo "✓ Python encontrado: $(python --version)"
    else
        echo "❌ Error: Python no está instalado"
        echo "Por favor instala Python 3.8 o superior"
        exit 1
    fi
}

# Función para verificar si pip está instalado
verificar_pip() {
    echo "Verificando instalación de pip..."
    if command -v pip3 &> /dev/null; then
        echo "✓ pip3 encontrado"
    elif command -v pip &> /dev/null; then
        echo "✓ pip encontrado"
    else
        echo "❌ Error: pip no está instalado"
        echo "Por favor instala pip"
        exit 1
    fi
}

# Función para crear entorno virtual
crear_entorno_virtual() {
    echo "Creando entorno virtual..."
    if [ ! -d "env" ]; then
        python3 -m venv env || python -m venv env
        echo "✓ Entorno virtual creado"
    else
        echo "✓ Entorno virtual ya existe"
    fi
}

# Función para activar entorno virtual
activar_entorno_virtual() {
    echo "Activando entorno virtual..."
    if [ -f "env/bin/activate" ]; then
        source env/bin/activate
        echo "✓ Entorno virtual activado"
    else
        echo "❌ Error: No se pudo activar el entorno virtual"
        exit 1
    fi
}

# Función para instalar dependencias
instalar_dependencias() {
    echo "Instalando dependencias..."
    pip install -r requirements.txt
    echo "✓ Dependencias instaladas"
}

# Función para ejecutar migraciones
ejecutar_migraciones() {
    echo "Ejecutando migraciones de base de datos..."
    python manage.py migrate
    echo "✓ Migraciones ejecutadas"
}

# Función para recopilar archivos estáticos
recopilar_estaticos() {
    echo "Recopilando archivos estáticos..."
    python manage.py collectstatic --no-input
    echo "✓ Archivos estáticos recopilados"
}

# Función para ejecutar el servidor
ejecutar_servidor() {
    echo ""
    echo "========================================"
    echo "   INICIANDO SERVIDOR DJANGO"
    echo "========================================"
    echo ""
    
    # Solicitar puerto al usuario
    read -p "Ingresa el puerto deseado (ejemplo: 3000, 8080, 9000) [8000]: " PORT
    PORT=${PORT:-8000}
    
    echo ""
    echo "Iniciando servidor en puerto $PORT..."
    echo "Accede a: http://127.0.0.1:$PORT/"
    echo ""
    echo "Para detener el servidor presiona Ctrl+C"
    echo ""
    
    python manage.py runserver $PORT
}

# Función principal para configurar todo
configurar_todo() {
    echo "Iniciando configuración completa del proyecto..."
    echo ""
    
    verificar_python
    verificar_pip
    crear_entorno_virtual
    activar_entorno_virtual
    instalar_dependencias
    ejecutar_migraciones
    recopilar_estaticos
    
    echo ""
    echo "✓ Configuración completada exitosamente!"
    echo ""
    
    # Preguntar si quiere ejecutar el servidor
    read -p "¿Deseas ejecutar el servidor ahora? (y/n) [y]: " EJECUTAR
    EJECUTAR=${EJECUTAR:-y}
    
    if [[ $EJECUTAR =~ ^[Yy]$ ]]; then
        ejecutar_servidor
    else
        echo "Para ejecutar el servidor más tarde, usa: $0 --run"
    fi
}

# Función para solo ejecutar el servidor
solo_ejecutar() {
    echo "Activando entorno virtual y ejecutando servidor..."
    activar_entorno_virtual
    ejecutar_servidor
}

# Función para solo configurar
solo_configurar() {
    echo "Configurando entorno del proyecto..."
    verificar_python
    verificar_pip
    crear_entorno_virtual
    activar_entorno_virtual
    instalar_dependencias
    ejecutar_migraciones
    recopilar_estaticos
    echo "✓ Configuración completada!"
}

# Procesar argumentos de línea de comandos
case "${1:-}" in
    -h|--help)
        mostrar_ayuda
        exit 0
        ;;
    -c|--clone)
        echo "Esta opción requiere que el repositorio ya esté clonado"
        echo "Para clonar un repositorio, usa: git clone <URL_DEL_REPOSITORIO>"
        exit 0
        ;;
    -s|--setup)
        solo_configurar
        ;;
    -r|--run)
        solo_ejecutar
        ;;
    -a|--all|"")
        configurar_todo
        ;;
    *)
        echo "Opción no válida: $1"
        echo "Usa -h o --help para ver las opciones disponibles"
        exit 1
        ;;
esac
