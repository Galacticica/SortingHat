from .models import College
from user_survey.models import UserResponse
from user_survey.helpers import get_user_response


def match(request):
    colleges = College.objects.all()
    user_response = get_user_response(request)
    colleges = filter_by_major(colleges, user_response)
    colleges = filter_by_price(colleges, user_response)
    colleges = filter_by_activity(colleges, user_response)
    colleges = filter_by_location(colleges, user_response)
    return colleges

def filter_by_major(colleges, user_response):
    colleges = colleges.filter(majors__name__in=user_response.majors)
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


