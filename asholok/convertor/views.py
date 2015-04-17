from django.shortcuts import render
from models import Engine
from my_auth.backends import PREPARED_BACKENDS

def index(request):
	return render(request, 'convertor/index.html', 
		{'engine': Engine(), 'available_backends': PREPARED_BACKENDS}
	)

def results(request):
	language = request.POST['language']
	currency = request.POST['currency']
	number = request.POST['number'].strip()

	return render(request, 'convertor/index.html', 
		{'engine': Engine(language, currency, number), 'available_backends': PREPARED_BACKENDS }
	)

# Create your views here.
