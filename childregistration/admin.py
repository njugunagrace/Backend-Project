from django.contrib import admin
from .models import ChildRegistration

# Register your models here.



class ChildAdmin(admin.ModelAdmin):
    list_display = ("id","child_name","date_of_birth","delayed_milestones", "guardian","sex")
admin.site.register(ChildRegistration, ChildAdmin)