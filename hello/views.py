from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib import messages
from django.shortcuts import render , redirect
from .models import Guntur,EG,WG,Krishna,Prakasam,Ananthapur,Kurnool,Visakha,Vizianagaram,Srikakulam,Kadapa,Chittoor,Nellore,contactus
#from api import excel
def home(request):
	return render(request, 'index.html', {})


def guntur(request):
	#guntur is a variable
    guntur = Guntur.objects.all()
    return render(request, 'guntur.html',
        {'guntur': guntur})

def eastgodavari(request):
	#guntur is a variable
    eastgodavari = EG.objects.all()
    return render(request, 'eastgodavari.html',
        {'eastgodavari': eastgodavari})



def westgodavari(request):
	#guntur is a variable
    westgodavari = WG.objects.all()
    return render(request, 'westgodavari.html',
        {'westgodavari': westgodavari})

def krishna(request):
	#guntur is a variable
    krishna = Krishna.objects.all()
    return render(request, 'krishna.html',
        {'krishna': krishna})




def prakasam(request):
	#guntur is a variable
    prakasam = Prakasam.objects.all()
    return render(request, 'prakasam.html',
        {'prakasam': prakasam})

def anantapur(request):
	#guntur is a variable
    ananthapur = Ananthapur.objects.all()
    return render(request, 'ananthapur.html',
        {'ananthapur': ananthapur})


def kurnool(request):
	#guntur is a variable
    kurnool = Kurnool.objects.all()
    return render(request, 'kurnool.html',
        {'kurnool': kurnool})

def visakhapatnam(request):
	#guntur is a variable
    visakha = Visakha.objects.all()
    return render(request, 'visakhapatnam.html',
        {'visakha': visakha})



def vizianagaram(request):
	#guntur is a variable
    vizianagaram = Vizianagaram.objects.all()
    return render(request, 'vizianagaram.html',
        {'vizianagaram': vizianagaram})

def srikakulam(request):
	#guntur is a variable
    srikakulam = Srikakulam.objects.all()
    return render(request, 'srikakulam.html',
        {'srikakulam': srikakulam})


def kadapa(request):
	#guntur is a variable
    kadapa = Kadapa.objects.all()
    return render(request, 'kadapa.html',
        {'kadapa': kadapa})

def chittoor(request):
	#guntur is a variable
    chittoor = Chittoor.objects.all()
    return render(request, 'chittoor.html',
        {'chittoor': chittoor})


def nellore(request):
	#guntur is a variable
    nellore = Nellore.objects.all()
    return render(request, 'nellore.html',
        {'nellore': nellore})

def contactus(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        contact = contactus(name=name,email=email,message=message)
        contact.save()
        messages.success("We have received your query!")
        return redirect('/')
    else :
        return render(request,'contactus.html',{})