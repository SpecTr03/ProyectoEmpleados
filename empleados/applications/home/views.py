from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/add.html'


class HomeTemplateView(TemplateView):
    template_name = 'home/home1.html'

class HomeTemplateView2(TemplateView):
    template_name = 'home/home2.html'

class HomeTemplateView3(TemplateView):
    template_name = 'home/home3.html' 


class InicioView(TemplateView):
    #pagina de inicio
    template_name = 'index.html'
