from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register Models here
app_name = 'core'
admin.site.register(CategoryComplaint)
admin.site.register(Complaint)