from django.contrib import admin
from .models import Complaint, CategoryComplaint
# Register your models here.

admin.site.register(Complaint)
admin.site.register(CategoryComplaint)
