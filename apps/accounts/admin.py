from django.contrib import admin
from accounts.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['dob']
    list_display_links = ['dob']

# admin.site.register(Profile)

