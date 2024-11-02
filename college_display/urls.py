from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path("<slug:slug>/", views.specific_college, name="college_preview"),
]