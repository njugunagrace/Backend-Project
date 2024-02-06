from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ngo.models import CustomUser,CommunityHealthVolunteer


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',"password")

class CommunityHealthVolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',"password" , 'gender', 'assigned_household')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CommunityHealthVolunteer, CommunityHealthVolunteerAdmin)
