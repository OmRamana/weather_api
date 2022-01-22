from multiprocessing import context
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_weather
from .form import SearchForm


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            return render(request, 'index.html', {'form': form, 's_query': s_query})
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form,})







     
    
    






""" 
class GetWeather(TemplateView):
    template_name = 'index.html'
    form_class = SearchForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            s_query = form.cleaned_data['search_query']
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form}) """


         

      
"""    def get_context_data(self, *args, **kwargs):
         data = get_weather()
         context ={
             'city':data[0],
             'discription':data[1],
             'temp':data[2],
             'temp_max': data[3],
         }
         return context """
