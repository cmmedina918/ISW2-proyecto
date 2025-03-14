from django.urls import path
from turnosApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('nuevoTurno/', views.nuevoTurno, name='nuevoTurno'),
    path('turnos/', views.turnosView, name='turnosList'),
    path('finalizarTurno/<int:turnoId>', views.finalizarTurno, name='finalizarTurno'),
]