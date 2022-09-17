from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from users.models import User

# class UserAdmin(BaseUserAdmin):
#     pass

# class TagInline(GenericTabularInline):
#     autocomplete_fields = ['tag']
#     model = TaggedItem

admin.site.register(User)
