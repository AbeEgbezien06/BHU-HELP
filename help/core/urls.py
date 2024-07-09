from django.contrib import admin
from django.urls import path
from .views import complaint

urlpatterns = [
    path('complaint/', complaint.as_view()),
]
