from django.contrib import admin
from django.urls import path
from .views import complaint, signup

urlpatterns = [
    path('complaint/', complaint.as_view()),
    path('signup/', signup, name='signup')
]
