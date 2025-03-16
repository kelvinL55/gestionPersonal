from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal
from .forms import PersonalForm

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
