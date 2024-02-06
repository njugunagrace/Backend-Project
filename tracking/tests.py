from django.test import TestCase
from tracking.models import SelfCareActivity, ParticipationInSocialLife, MovingAbility, DailyLiving

class ModelsTestCase(TestCase):
    def test_self_care_activity_total(self):
        self_care = SelfCareActivity(
            bathing=3,
            using_toilet=4,
            dressing=2,
            eating=5
        )
        self_care.save()
        self.assertEqual(self_care.calculate_total(), 14)  

    def test_participation_in_social_life_total(self):
        social_life = ParticipationInSocialLife(
            school=5,
            friends=3,
            religious_places=2,
            leisure=4
        )
        social_life.save()
        self.assertEqual(social_life.calculate_total(), 14)  
    def test_moving_ability_total(self):
        moving_ability = MovingAbility(
            inside_the_house=4,
            around_the_house=3,
            in_the_block=5,
            far_outside=2
        )
        moving_ability.save()
        self.assertEqual(moving_ability.calculate_total(), 14)  
    def test_daily_living_total(self):
        daily_living = DailyLiving(
            chore_activities=3,
            cooking=4,
            washing=2,
            playing=5
        )
        daily_living.save()
        self.assertEqual(daily_living.calculate_total(), 14)  
