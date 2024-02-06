from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    groups = models.ManyToManyField(Group, related_name='custom_users')  
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    is_NGO = models.BooleanField(default=True)  
    password = models.CharField(max_length=128)

class CommunityHealthVolunteer(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(Group, related_name='healthworkers')  
    gender_choices = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    gender = models.CharField(max_length=10, choices=gender_choices)
    assigned_household = models.PositiveIntegerField(default=0)
    user_permissions = models.ManyToManyField(Permission, related_name='healthworkers')
    is_healthworker = models.BooleanField(default=True)  
    password = models.CharField(max_length=128)
