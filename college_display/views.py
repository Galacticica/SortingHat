from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import College
from user_survey.models import UserResponse
from user_survey.helpers import get_user_response
from .sort_schools import match, matching_majors, matching_activities

def index(request):
    template = loader.get_template('college_display/index.html')
    colleges = match(request)
    context = {"colleges" : colleges}
    return HttpResponse(template.render(context, request))


def specific_college(request, slug):
    college_to_view = get_object_or_404(College, slug=slug)
    template = loader.get_template('college_display/college.html')
    price = '${:,}'.format(college_to_view.price)
    population = '{:,}'.format(college_to_view.population)
    majors = matching_majors(request, college_to_view)
    activities = matching_activities(request, college_to_view)
    context = {"college" : college_to_view, "price" : price, "population" : population, "majors" : majors, "activities" : activities}
    return HttpResponse(template.render(context, request))