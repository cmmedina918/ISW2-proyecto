from django.shortcuts import render, redirect, get_object_or_404
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

def turnosPendientesView(request):
    turnosList = Turno.objects.all().filter(status=0).order_by('fecha_turno')
    return render(request, 'turnosPendientes.html', {'turnos': turnosList})

def turnosFinalizadosView(request):
    turnosList = Turno.objects.all().filter(status=1).order_by('fecha_turno')
    return render(request, 'turnosFinalizados.html', {'turnos': turnosList})

def finalizarTurno(request, turnoId):
    turno = get_object_or_404(Turno, id=turnoId)
    turno.status = 1
    turno.save()
    return redirect('turnosList')
