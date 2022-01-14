from multiprocessing import context
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_weather

class GetWeather(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
         data = get_weather()
         context ={
             'city':data[0],
             'discription':data[1],
             'temp':data[2],
             'temp_max': data[3],
         }
         return context
# Create your views here.
