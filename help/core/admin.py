from django.contrib import admin
from .models import Complaint, CategoryComplaint
from django import forms



admin.site.register(Complaint)
admin.site.register(CategoryComplaint)
