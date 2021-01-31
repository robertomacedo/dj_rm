from django.http import HttpResponse
#from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<html><body><h1>Curso de Django</h1></body></html>')
