from django.shortcuts import render,redirect
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def nuevoTurno(request):
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevoTurno')
    else:
        form = turnoForm()
        return render(request, 'forms/turno.html', {'form': form})