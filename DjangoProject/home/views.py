from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'page' : 'Home page'}
    return render(request, "index.html", context=context)
    
def about(request):
    context = {'page' : 'About page'}
    return render(request, "about.html", context=context)

def contanct(request):
    context = {'page' : 'Contanct page'}
    return render(request, "contanct.html", context=context)
