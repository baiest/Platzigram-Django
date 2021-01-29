from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user', 'phone_number')