#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic



class Home(generic.TemplateView):
    template_name = "indexx.html"