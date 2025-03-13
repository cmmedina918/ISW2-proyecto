from django.urls import path
from turnosApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('nuevoTurno/', views.nuevoTurno, name='nuevoTurno')
]