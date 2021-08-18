from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render
from .models import Guntur,EG
#from api import excel
def home(request):
	return render(request, 'index.html', {})

def guntur(request):
	#guntur is a variable
    guntur = Guntur.objects.all()
    return render(request, 'guntur.html',
        {'guntur': guntur})

def EG(request):
	#guntur is a variable
    eg = EG.objects.all()
    return render(request, 'guntur.html',
        {'EG': eg})