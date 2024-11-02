from .models import College
from user_survey.models import UserResponse
from user_survey.helpers import get_user_response
from django.db.models import Q



def match(request):
    '''
    This function takes all of the colleges in the database and filters them based on the user's responses to the questionnaire
    '''
    colleges = College.objects.all()
    user_response = get_user_response(request)
    colleges = filter_by_major(colleges, user_response)
    colleges = filter_by_price(colleges, user_response)
    colleges = filter_by_activity(colleges, user_response)
    colleges = filter_by_location(colleges, user_response)
    colleges = filter_by_population(colleges, user_response)
    return colleges

def filter_by_major(colleges, user_response):
    colleges.filter(Q(majors__name__in=user_response.majors)).distinct()
    return colleges

def filter_by_price(colleges, user_response):
    min_price, max_price = (user_response.price_range).split()
    colleges = colleges.filter(price__gte=min_price, price__lte=max_price)
    return colleges

def filter_by_activity(colleges, user_response):
    if user_response.activity_cats != []:
        colleges = colleges.filter(activities__category__in=user_response.activity_cats).distinct()
    return colleges

def filter_by_location(colleges, user_response):
    if user_response.in_state == True:
        colleges = colleges.filter(state=user_response.state)
    else:
        colleges = colleges.exclude(state=user_response.state)
    return colleges

def filter_by_population(colleges, user_response):
    print(user_response.population_range)
    min_pop, max_pop = (user_response.population_range).split()
    colleges = colleges.filter(population__gte=min_pop, population__lte=max_pop)
    return colleges


def matching_majors(request, college):
    offered_majors = [major.name for major in college.majors.all()]
    user_response = get_user_response(request)
    wanted_majors = user_response.majors
    overlap = []
    for major in offered_majors:
        if major in wanted_majors:
            overlap.append(major)
    return overlap

def matching_activities(request, college):
    offered_activities = college.activities.all()
    user_response = get_user_response(request)
    wanted_activities = user_response.activity_cats
    overlap = []
    if 'Sports' in wanted_activities:
        sports = offered_activities.filter(category='Sports')
        overlap.extend(sports)
    if 'Arts' in wanted_activities:
        arts = offered_activities.filter(category='Arts')
        overlap.extend(arts)
    if 'Professional' in wanted_activities:
        professional = offered_activities.filter(category='Professional')
        overlap.extend(professional)
    return overlap