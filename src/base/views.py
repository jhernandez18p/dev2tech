from django.shortcuts import render
from django.views.generic import ListView

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'app/home.html'
