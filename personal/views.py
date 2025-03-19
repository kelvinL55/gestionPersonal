from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal
from .forms import PersonalForm
import pandas as pd
from django.contrib import messages
from django.urls import reverse


def personal_list(request):
    personal = Personal.objects.all()
    return render(request, 'personal/personal_list.html', {'personal': personal})

def personal_create(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'personal/personal_form.html', {'form': form})

def personal_update(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=persona)
    return render(request, 'personal/personal_form.html', {'form': form})

def personal_delete(request, pk):
    persona = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personal_list')
    return render(request, 'personal/personal_confirm_delete.html', {'personal': persona})

def import_excel(request):
    if request.method == 'POST':
        # Verificar si se subió un archivo
        if 'excel_file' not in request.FILES:
            messages.error(request, 'Por favor seleccione un archivo Excel')
            return redirect('personal_list')
            
        excel_file = request.FILES['excel_file']
        
        # Verificar la extensión del archivo
        if not excel_file.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'El archivo debe ser un Excel (.xlsx o .xls)')
            return redirect('personal_list')
        
        try:
            # Leer el archivo Excel
            df = pd.read_excel(excel_file)
            
            # Verificar que las columnas requeridas existan
            required_columns = ['N°', 'Código', 'Nombre', 'Ubicación', 'G - GRUPO', 'Categorias']
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                messages.error(request, f'El archivo Excel no contiene las siguientes columnas requeridas: {", ".join(missing_columns)}')
                return redirect('personal_list')
            
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
            
        return redirect('personal_list')
        
    # Si no es POST, redirigir a la vista de lista
    return redirect('personal_list')

def home(request):
    return render(request, 'personal/home.html')

def listado(request):
    personal = Personal.objects.all()
    return render(request, 'personal/listado.html', {'personal': personal})

def personal_delete_all(request):
    if request.method == 'POST':
        Personal.objects.all().delete()
        messages.success(request, 'Se han eliminado todos los registros correctamente')
        return redirect('personal_list')
    return render(request, 'personal/personal_delete_all.html')
