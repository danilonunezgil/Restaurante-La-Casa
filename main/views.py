from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "base.html")
    #return HttpResponse('<h1>It worked!</h1>'
     #                   '<div>Made by <a href="http://encisosystems.com" target="_blank">Enciso Systems</a></div>')
