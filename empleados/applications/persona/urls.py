from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-empleados-area/<short_name>', views.ListByArea.as_view(), name='empleados_by_area'),
    path('listar-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_by_lista'),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='add_empleado'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]

