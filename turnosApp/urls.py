
from django.urls import path
from django.contrib.auth import views as auth_views
from turnosApp import views
from turnosApp.forms import CustomLoginForm

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
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
        authentication_form=CustomLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]