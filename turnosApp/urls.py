from django.urls import path
from turnosApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('nuevoTurno/', views.nuevoTurno, name='nuevoTurno'),
    path('turnos/', views.turnosPendientesView, name='turnosList'),
    path('turnosFinalizados/', views.turnosFinalizadosView, name='turnosFinalizados'),
    path('finalizarTurno/<int:turnoId>', views.finalizarTurno, name='finalizarTurno'),
    path('filtrar-medicos/', views.filtrar_medicos, name='filtrar_medicos'),
    path('nuevoPaciente/',views.nuevoPaciente, name='nuevoPaciente'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('deactivatePaciente/<int:pacienteId>', views.deactivatePaciente, name='deactivatePaciente'),

]