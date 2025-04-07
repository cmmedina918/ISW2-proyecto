
from django.contrib.auth.decorators import login_required, login_not_required
from django.db.models.functions import Concat
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.db.models import Value, CharField
from .models import Turno, Medico

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html',{})

@login_not_required
def nuevoTurno(request):
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnosList')
        else:
            return render(request,
                          "forms/turno.html",
                          {'form': form})
    else:
        form = turnoForm()

    return render(request,
                  'forms/turno.html',
                  {'form': form})

@login_required
def turnosPendientesView(request):
    medico_actual = request.user.id
    turnosList = Turno.objects.all().filter(status = 0, medico_id = medico_actual ).order_by('fecha_turno')
    return render(request, 'turnosPendientes.html', {'turnos': turnosList})

@login_required
def turnosFinalizadosView(request):
    medico_actual = request.user.id
    turnosList = Turno.objects.all().filter(status=1, medico_id = medico_actual).order_by('fecha_turno')
    return render(request, 'turnosFinalizados.html', {'turnos': turnosList})

@login_required
def finalizarTurno(request, turnoId):
    turno = get_object_or_404(Turno, id=turnoId)
    turno.status = 1
    turno.save()
    return redirect('turnosList')

@login_not_required
def filtrar_medicos(request):
    especialidad_id = request.GET.get('especialidad_id')

    if especialidad_id:
        medicos = Medico.objects.filter(especialidades__id=especialidad_id).annotate(
            nombre_completo=Concat('user__first_name', Value(' '), 'user__last_name', output_field=CharField())
        ).values('user_id', 'nombre_completo')  # Usamos 'user_id'
    else:
        medicos = Medico.objects.all().annotate(
            nombre_completo=Concat('user__first_name', Value(' '), 'user__last_name', output_field=CharField())
        ).values('user_id', 'nombre_completo')  # Usamos 'user_id'

    return JsonResponse(list(medicos), safe=False)

@login_not_required
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

@login_required
def pacientes(request):
    pacienteList = Paciente.objects.all().filter(status=0)
    return render(request, 'pacientes.html', {'pacientes': pacienteList})

@login_required
def deactivatePaciente(request, pacienteId):
    paciente = get_object_or_404(Paciente, id=pacienteId)
    paciente.status = 1
    paciente.save()
    return redirect('pacientes')