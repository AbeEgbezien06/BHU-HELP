from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register Models here

admin.site.register(CategoryComplaint)
admin.site.register(Complaint)