from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def expo(request):
    template=loader.get_template('expo.html')
    return HttpResponse(template.render())