from django.db import models
from datetime import date
from guardian.models import Guardian


class ChildRegistration(models.Model):
    child_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    
    SEX_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    
    DELAYED_MILESTONES_CHOICES = (
        ('Cannot Sit', 'Cannot Sit'),
        ('Cannot Walk', 'Cannot Walk'),
        ('Cannot Move Head', 'Cannot Move Head'),
        ('Cannot Use Hands', 'Cannot Use Hands'),
        ('Other', 'Other')
    )
    delayed_milestones = models.CharField(max_length=128, choices=DELAYED_MILESTONES_CHOICES)
    guardian = models.ForeignKey(Guardian, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def age(self):
        today = date.today()
        birth_date = self.date_of_birth
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age


    def __str__(self):
        return f"{self.child_name}, Age: {self.age()})"
        
