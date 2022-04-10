from django import views
from django.urls import path
from . import views

app_name ='home_app'

urlpatterns = [
    #incluimos las urls de la app home
    path('', views.InicioView.as_view(), name='index'),
    path('prueba/', views.PruebaView.as_view()),
    path('home1/', views.HomeTemplateView.as_view(), name='home1'),
    path('home2/', views.HomeTemplateView2.as_view(), name='home2'),
    path('home3/', views.HomeTemplateView3.as_view(), name='home3'),
]
