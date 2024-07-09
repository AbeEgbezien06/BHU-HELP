from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

# Register Models here

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('email', 'phone_number', 'room_number', 'hostel')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
