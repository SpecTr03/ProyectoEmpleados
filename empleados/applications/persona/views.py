from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado, DepartamentoModelo, Habilidades
# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            #Buscamos por cadena, ejemplo= si buscamos jo el icontains se encargara de buscar todos los nombres
            #que contangan la j y la o al principio
            full_name__icontains=palabra_clave
        )
        return lista
    
    
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/list_empleados_admin.html'
    paginate_by = 10
    ordering = 'first_name'
    model = Empleado


class ListByArea(ListView):
    #Listar empleados de un area
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        parametro = self.kwargs["short_name"]
        lista = Empleado.objects.filter(
        departamento__short_name = parametro
    )
        return lista


class ListEmpleadosByKword(ListView):
    #lista de empleados por palabra clave
    template_name='persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #aqui obtengo el input del html a traves de un get
        palabra_clave = self.request.GET.get("kword", "")
        print ('=====', palabra_clave)
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


class SuccessView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields = ['first_name','last_name','job']
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]

    #validacion de los datos
    def form_valid(self, form):
        empleado = form.save()
        #aqui completo los datos del full name concatenando el first_name y el last_name
        empleado.full_name = empleado.first_name + '' + empleado.last_name
        
        print(empleado.first_name)
        return super(EmpleadoCreateView, self).form_valid(form)
    success_url = reverse_lazy('persona_app:correcto')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ('__all__')
    success_url = reverse_lazy('persona_app:correcto')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:correcto')
    