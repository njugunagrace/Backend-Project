from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Guardian(models.Model):
    parent_name = models.CharField(max_length=64)  
    national_id = models.CharField(max_length=32, unique=True)
    number_of_children = models.PositiveIntegerField()
    is_eligible = models.BooleanField()
    phone_number = PhoneNumberField()
    location = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.parent_name


    

