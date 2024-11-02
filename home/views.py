from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('home/main.html')
  context={}
  return HttpResponse(template.render(context, request))