from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import College
from user_survey.models import UserResponse
from user_survey.helpers import get_user_response
from .sort_schools import match

def index(request):
    # template = loader.get_template('college_display/index.html')
    print(match(request))
