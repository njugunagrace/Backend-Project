from django.contrib import admin
from .models import SelfCareActivity, ParticipationInSocialLife, MovingAbility, DailyLiving


class ParticipationInSocialLifeAdmin(admin.ModelAdmin):
    list_display = ("school", "friends", "religious_places", "leisure", "child","total", "created_at", "updated_at")
admin.site.register(ParticipationInSocialLife, ParticipationInSocialLifeAdmin)   


class MovingAbilityAdmin(admin.ModelAdmin):
    list_display = ("inside_the_house", "around_the_house", "in_the_block", "far_outside","child", "total", "created_at", "updated_at")
admin.site.register(MovingAbility, MovingAbilityAdmin)   


class DailyLivingAdmin(admin.ModelAdmin):
    list_display = ("chore_activities", "cooking", "washing", "playing", "child", "total", "created_at", "updated_at")
admin.site.register( DailyLiving,  DailyLivingAdmin) 


class SelfCareActivityAdmin(admin.ModelAdmin):
    list_display= ("bathing", "using_toilet", "dressing", "eating", "child", "total", "created_at", "updated_at")
admin.site.register(SelfCareActivity, SelfCareActivityAdmin) 







