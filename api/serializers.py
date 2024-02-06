from rest_framework import serializers
from tracking.models import DailyLiving
from tracking.models import SelfCareActivity
from tracking.models import MovingAbility
from tracking.models import ParticipationInSocialLife
from childregistration.models import ChildRegistration
from tracking.models import DailyLiving
from tracking.models import SelfCareActivity
from tracking.models import MovingAbility
from tracking.models import ParticipationInSocialLife
from childregistration.models import ChildRegistration
from ngo.models import CustomUser
from guardian.models import Guardian
from ngo.models import CommunityHealthVolunteer



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id",'username', 'email', 'first_name', 'last_name')


class CommunityHealthVolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityHealthVolunteer
        fields = ("username", "first_name", "last_name", "phone_number", "gender", "password")


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildRegistration
        fields = '__all__'        


class DailyLivingSerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.child_name', read_only=True)

    class Meta:
        model = DailyLiving
        fields = '__all__'



class SelfcareActivitySerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.child_name', read_only=True)

    class Meta:
        model = SelfCareActivity
        fields = '__all__'


class MovingAbilitySerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.child_name', read_only=True)

    class Meta:
        model = MovingAbility
        fields = '__all__'

class ParticipationSerializer(serializers.ModelSerializer):
    child_name = serializers.CharField(source='child.child_name', read_only=True)

    class Meta:
        model = ParticipationInSocialLife
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)

    class Meta:
        model = Guardian
        fields = '__all__'


class GuardianListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ("id", "parent_name", "national_id", "number_of_children", "is_eligible", "phone_number","location", "created_at", "updated_at")

