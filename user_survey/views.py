from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import UserResponse
from .helpers import get_user_response, save_user_response
# Create your views here.



def MajorFormView(request):
    question = "What majors are you interested in? (select up to 5)"
    form = MajorSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        user_response.majors = [major.name for major in form.cleaned_data['major_query']]
        save_user_response(request, user_response)
        return redirect(PriceFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text}
    return HttpResponse(template.render(context, request))


def PriceFormView(request):
    question = "What price range are you looking for?"
    form = PriceSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    description = "This is for one year's tuition, room, and dining."
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        user_response.price_range = form.cleaned_data['price_query']
        save_user_response(request, user_response)
        return redirect(SportFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text, "description" : description}
    return HttpResponse(template.render(context, request))

def SportFormView(request):
    question = "Are you interested in participating in any sports?"
    form = SportSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['sport_query'] == 'yes':
            user_response.activity_cats.append('Sports')
        save_user_response(request, user_response)
        return redirect(ArtsFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text}
    return HttpResponse(template.render(context, request))

def ArtsFormView(request):
    question = "Are you interested in participating in any clubs related to the arts?"
    form = ArtsSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    description = "This includes music, art, drama, etc."
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['arts_query'] == 'yes':
            user_response.activity_cats.append('Arts')
        save_user_response(request, user_response)
        return redirect(ProfessionalClubFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text, "description" : description}
    return HttpResponse(template.render(context, request))

def ProfessionalClubFormView(request):
    question = "Are you interested in participating in any clubs related to specific majors?"
    form = ProfessionalSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    description = "This includes business, agriculture, programming, etc."
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['professional_query'] == 'yes':
            user_response.activity_cats.append('Professional')
        save_user_response(request, user_response)
        return redirect(HomeLocationFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text, "description" : description}
    return HttpResponse(template.render(context, request))

def HomeLocationFormView(request):
    question = "Where are you coming from?"
    form = CityStateSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        user_response.city = form.cleaned_data['city_query']
        user_response.state = form.cleaned_data['state_query']
        save_user_response(request, user_response)
        return redirect(InStateFormView)
    context = {"question" : question, "form" : form, "submit" : search_button_text}
    return HttpResponse(template.render(context, request))

def InStateFormView(request):
    question = "Are you looking for a school in state?"
    form = InStateSearch(request.POST)
    template = loader.get_template("user_survey/question.html")
    search_button_text = "Next Question"
    user_response = get_user_response(request)
    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['in_state_query'] == 'yes':
            user_response.in_state = True
        else:
            user_response.in_state = False
        save_user_response(request, user_response)
        return redirect('index')
    context = {"question" : question, "form" : form, "submit" : search_button_text}
    return HttpResponse(template.render(context, request))

