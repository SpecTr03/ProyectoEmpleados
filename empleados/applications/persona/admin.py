from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class adminEmpleado(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job'
    )
    search_fields = (
        'first_name',
    )
    list_filter = (
        'job',
    )
    filter_horizontal = (
        'habilidades',
    )
admin.site.register(Empleado,adminEmpleado)

