from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal
from .forms import PersonalForm
import pandas as pd
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

# Función de comprobación para verificar si el usuario es staff o superusuario
# Esta función se usará como decorador para restringir el acceso a ciertas vistas.
def es_gestor(user):
    """
    Comprueba si el usuario tiene permisos de gestor (staff o superusuario).

    Args:
        user: El objeto de usuario de Django.

    Returns:
        bool: True si el usuario es staff o superusuario, False en caso contrario.
    """
    return user.is_staff or user.is_superuser

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si el usuario no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def personal_list(request):
    """
    Vista para listar todos los registros de personal.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza la plantilla con la lista de personal
    """
    personal = Personal.objects.all()
    return render(request, 'personal/tabla.html', {'personal': personal})

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def personal_create(request):
    """
    Vista para crear un nuevo registro de personal.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza el formulario o redirecciona a la lista
    """
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal:personal_list')
    else:
        form = PersonalForm()
    return render(request, 'personal/formulario.html', {'form': form})

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def personal_update(request, pk):
    """
    Vista para actualizar un registro de personal existente.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        pk: Clave primaria del registro a actualizar
        
    Returns:
        HttpResponse: Renderiza el formulario o redirecciona a la lista
    """
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('personal:personal_list')
    else:
        form = PersonalForm(instance=persona)
    return render(request, 'personal/formulario.html', {'form': form})

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def personal_delete(request, pk):
    """
    Vista para eliminar un registro de personal.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        pk: Clave primaria del registro a eliminar
        
    Returns:
        HttpResponse: Redirecciona a lista después de eliminar
    """
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personal:personal_list')
    return redirect('personal:personal_list')

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def import_excel(request):
    """
    Vista para importar datos desde un archivo Excel.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Redirecciona a la lista de personal
    """
    if request.method == 'POST':
        # Verificar si se subió un archivo
        if 'excel_file' not in request.FILES:
            messages.error(request, 'Por favor seleccione un archivo Excel')
            return redirect('personal:personal_list')
            
        excel_file = request.FILES['excel_file']
        
        # Verificar la extensión del archivo
        if not excel_file.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'El archivo debe ser un Excel (.xlsx o .xls)')
            return redirect('personal:personal_list')
        
        try:
            # Leer el archivo Excel
            df = pd.read_excel(excel_file)
            
            # Verificar que las columnas requeridas existan
            required_columns = ['N°', 'Código', 'Nombre', 'Ubicación', 'G - GRUPO', 'Categorias']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                messages.error(request, f'El archivo Excel no contiene las siguientes columnas requeridas: {", ".join(missing_columns)}')
                return redirect('personal:personal_list')
            
            # Procesar cada fila
            records_imported = 0
            for index, row in df.iterrows():
                try:
                    # Verificar si existe un registro con el mismo código
                    existing_record = Personal.objects.filter(codigo=row['Código']).first()
                    
                    if existing_record:
                        # Actualizar registro existente
                        existing_record.nombre = row['Nombre']
                        existing_record.ubicacion = row['Ubicación']
                        existing_record.numero = row['N°']
                        existing_record.grupo = row['G - GRUPO']
                        existing_record.categorias = row['Categorias']
                        existing_record.save()
                    else:
                        # Crear nuevo registro
                        Personal.objects.create(
                            numero=row['N°'],
                            codigo=row['Código'],
                            nombre=row['Nombre'],
                            ubicacion=row['Ubicación'],
                            grupo=row['G - GRUPO'],
                            categorias=row['Categorias']
                        )
                    
                    records_imported += 1
                except Exception as e:
                    # Registrar errores individuales de fila pero continuar procesando
                    print(f"Error al importar la fila {index}: {str(e)}")
                    messages.error(request, f'Error en la fila {index + 2}: {str(e)}')
                    continue
            
            if records_imported > 0:
                messages.success(request, f'Se importaron {records_imported} registros correctamente')
            else:
                messages.warning(request, 'No se importó ningún registro')
            
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            
        return redirect('personal:personal_list')
        
    # Si no es POST, redirigir a la vista de lista
    return redirect('personal:personal_list')

def home(request):
    """
    Vista para la página principal.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza la plantilla home.html
    """
    return render(request, 'personal/inicio.html')

@login_required(login_url='usuarios:login')
# Eliminar el decorador user_passes_test de aquí, 
# ya que esta vista debe ser accesible para user001.
# @user_passes_test(es_gestor, login_url='personal:home') 
def listado(request):
    """
    Vista para mostrar un listado alternativo de personal.
    Requiere autenticación (pero no permisos de gestor).
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza la plantilla con el listado
    """
    personal = Personal.objects.all()
    return render(request, 'personal/vista_alterna.html', {'personal': personal})

@login_required(login_url='usuarios:login')
# Redirigir a 'personal:listado' si no es gestor
@user_passes_test(es_gestor, login_url='personal:listado')
def personal_delete_all(request):
    """
    Vista para eliminar todos los registros de personal.
    Requiere autenticación y permisos de gestor.
    
    Args:
        request: Objeto HttpRequest
        
    Returns:
        HttpResponse: Renderiza confirmación o redirecciona a lista
    """
    if request.method == 'POST':
        Personal.objects.all().delete()
        messages.success(request, 'Se han eliminado todos los registros correctamente')
        return redirect('personal:personal_list')
    # Si no es POST, redirigir a la lista de gestión (solo accesible por gestores)
    # o a 'personal:listado' si se prefiere como fallback general. 
    # Optamos por personal_list ya que la acción se origina desde ahí.
    return redirect('personal:personal_list')
