from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import MajorSearch
# Create your views here.

def MajorFormView(request):
    question = "What majors are you interested in? (select up to 5)"
    form = MajorSearch(request.GET)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    context = {"question" : question, "form" : form, "submit" : search_button_text}
    return HttpResponse(template.render(context, render))
