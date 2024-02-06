from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models
from childregistration.models import ChildRegistration

class BaseTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BaseScoring(models.Model):
    def validate_total(self, total, max_total=20):
        if total < 0 or total > max_total:
            raise ValidationError(f"Total score must be between 0 and {max_total}.")

    class Meta:
        abstract = True

class SelfCareActivity(BaseTime, BaseScoring):
    bathing = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    using_toilet = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    dressing = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    eating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    child = models.OneToOneField(ChildRegistration, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)


    def calculate_total(self):
        return self.bathing + self.using_toilet + self.dressing + self.eating

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()  
        self.validate_total(self.total)
        super(SelfCareActivity, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.total) 


class ParticipationInSocialLife(BaseTime, BaseScoring):
    school = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    friends = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    religious_places = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    leisure = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    child = models.OneToOneField(ChildRegistration, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)

    def calculate_total(self):
        return self.school + self.friends + self.religious_places + self.leisure  

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        self.validate_total(self.total)
        super(ParticipationInSocialLife, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.total)     


class MovingAbility(BaseTime, BaseScoring):
    inside_the_house = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    around_the_house = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    in_the_block = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    far_outside = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    child = models.OneToOneField(ChildRegistration, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)

    def calculate_total(self):
        return self.inside_the_house + self.around_the_house + self.in_the_block + self.far_outside 

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        self.validate_total(self.total)
        super(MovingAbility, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.total)    

class DailyLiving(BaseTime, BaseScoring):
    chore_activities = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    cooking = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    washing = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    playing = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    child = models.OneToOneField(ChildRegistration, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)

    def calculate_total(self):
        return self.chore_activities + self.cooking + self.washing + self.playing  

    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        self.validate_total(self.total)
        super(DailyLiving, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.total)  


 
