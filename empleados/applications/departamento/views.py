from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import DepartamentoModelo

# Create your views here.

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = DepartamentoModelo
    

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:listar_departamento')

    def form_valid(self, form):
        print('formvalue')
        
        #1 manera de usar la ORM para guardar datos
        depa = DepartamentoModelo(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['nombre_corto']
        )
        depa.save()

        #2 manera de usar la ORM para guardar datos
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa 
        )
        return super(NewDepartamentoView, self).form_valid(form)