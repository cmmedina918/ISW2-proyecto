from datetime import date
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Turno, Medico

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
            return render(request, "forms/turno.html",
                          {"form": form})
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


def filtrar_medicos(request):
    especialidad_id = request.GET.get('especialidad_id')

    if especialidad_id:
        medicos = Medico.objects.filter(especialidades__id=especialidad_id).values('id', 'nombre')
    else:
        medicos = Medico.objects.all().values('id', 'nombre')

    return JsonResponse(list(medicos), safe=False)

def nuevoPaciente(request):
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes')
        else:
            return render(request, 'forms/paciente.html', {'form': form})
    else:
        form = pacienteForm()

    return render(request, 'forms/paciente.html', {'form': form})

def pacientes(request):
    pacienteList = Paciente.objects.all().filter(status=0)
    return render(request, 'pacientes.html', {'pacientes': pacienteList})

def deactivatePaciente(request, pacienteId):
    paciente = get_object_or_404(Paciente, id=pacienteId)
    paciente.status = 1
    paciente.save()
    return redirect('pacientes')