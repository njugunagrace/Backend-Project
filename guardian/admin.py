from django.contrib import admin
from .models import Guardian

class GuardianAdmin(admin.ModelAdmin):
  list_display = ("parent_name","national_id","number_of_children","is_eligible","phone_number", "location")

admin.site.register(Guardian,GuardianAdmin)