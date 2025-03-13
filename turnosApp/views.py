from django.shortcuts import render,redirect
from .forms import *
from .models import Turno

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def nuevoTurno(request):
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnosList')
    else:
        form = turnoForm()
        return render(request, 'forms/turno.html', {'form': form})

def turnosView(request):
    turnosList = Turno.objects.all()
    return render(request, 'turnos.html',{'turnos': turnosList})