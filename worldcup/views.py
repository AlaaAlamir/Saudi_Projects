from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def saudi2034(request):
    template=loader.get_template('saudi2034.html')
    return HttpResponse(template.render())