from .models import UserResponse

def get_user_response(request):
    user_response_data = request.session.get('user_response', {})
    return UserResponse.from_dict(user_response_data)

def save_user_response(request, user_response):
    request.session['user_response'] = user_response.to_dict()