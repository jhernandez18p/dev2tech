from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
		'title' : 'Hola mundo',
		'pg_title' : 'Home',
	}
	return render(request, 'home.html', context)
