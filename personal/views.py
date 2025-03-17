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
        # Check if a file was uploaded
        if 'excel_file' not in request.FILES:
            messages.error(request, 'Por favor seleccione un archivo Excel')
            return redirect('personal_list')  # Adjust this to your actual view name
            
        excel_file = request.FILES['excel_file']
        
        # Check file extension
        if not excel_file.name.endswith(('.xlsx', '.xls')):
            messages.error(request, 'El archivo debe ser un Excel (.xlsx o .xls)')
            return redirect('personal_list')  # Adjust this to your actual view name
        
        try:
            # Read the Excel file
            df = pd.read_excel(excel_file)
            
            # Process each row
            records_imported = 0
            for index, row in df.iterrows():
                try:
                    # Check if record with same code already exists
                    existing_record = Personal.objects.filter(codigo=row['Código']).first()
                    
                    if existing_record:
                        # Update existing record
                        existing_record.nombre = row['Nombre']
                        existing_record.ubicacion = row['Ubicación']
                        existing_record.numero = row['N°']
                        existing_record.save()
                    else:
                        # Create new record
                        Personal.objects.create(
                            numero=row['N°'],
                            codigo=row['Código'],
                            nombre=row['Nombre'],
                            ubicacion=row['Ubicación']
                        )
                    
                    records_imported += 1
                except Exception as e:
                    # Log individual row errors but continue processing
                    print(f"Error importing row {index}: {str(e)}")
                    continue
            
            messages.success(request, f'Se importaron {records_imported} registros correctamente')
            
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            
        return redirect('personal_list')  # Adjust this to your actual view name
        
    # If not POST, redirect to list view
    return redirect('personal_list')  # Adjust this to your actual view name

def home(request):
    return render(request, 'personal/home.html')

def listado(request):
    personal = Personal.objects.all()
    return render(request, 'personal/listado.html', {'personal': personal})
