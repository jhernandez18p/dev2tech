from django.shortcuts import render

# Create your views here.
def home(request):

    context = {
        'title':'Home',
        'nombre':'Josmer Hernandez'
    }

    return render(request, 'frontend/index.html',context)
