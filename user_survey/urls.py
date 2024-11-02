from django.urls import path
from . import views

urlpatterns = [
    path('question_1/', views.MajorFormView, name='Major'),
    path('question_2/', views.PriceFormView, name='Price'),
    path('question_3/', views.SportFormView, name='Sport'),
    path('question_4/', views.ArtsFormView, name='Arts'),
    path('question_5/', views.ProfessionalClubFormView, name='Professional Clubs'),
    path('question_6/', views.HomeLocationFormView, name='HomeLocation'),
    path('question_7/', views.InStateFormView, name='In State')
]