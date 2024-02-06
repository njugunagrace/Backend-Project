from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from ngo.models import CustomUser, CommunityHealthVolunteer
from .serializers import CustomUserSerializer,CommunityHealthVolunteerSerializer
from .permissions import IsAdminOrReadOnly,IsOwnerOrAdmin,IsAdminOrNGO,IsHealthVolunteer
from http.client import NOT_FOUND
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import DailyLivingSerializer
from .serializers import SelfcareActivitySerializer
from .serializers import ParticipationSerializer
from .serializers import MovingAbilitySerializer
from tracking.models import  ParticipationInSocialLife, MovingAbility, SelfCareActivity, DailyLiving
from rest_framework.response import Response
from guardian.models import Guardian
from .serializers import GuardianSerializer,GuardianListSerializer
from childregistration.models import ChildRegistration
from .serializers import ChildSerializer
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotFound

#User views

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': 'NGO user created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username).first()
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid login details'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_logout(request):
    logout(request)
    return Response({'message': 'NGO user logged out successfully'}, status=status.HTTP_200_OK)
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]
class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]
class CommunityHealthVolunteerList(generics.ListCreateAPIView):
    queryset = CommunityHealthVolunteer.objects.all()
    serializer_class = CommunityHealthVolunteerSerializer
    permission_classes = [IsAdminOrReadOnly]

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrAdmin])
def chv_detail(request, pk):
    try:
        chv = CommunityHealthVolunteer.objects.get(pk=pk)
    except CommunityHealthVolunteer.DoesNotExist:
        return Response({'message': 'CHV not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CommunityHealthVolunteerSerializer(CommunityHealthVolunteer)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = CommunityHealthVolunteerSerializer(CommunityHealthVolunteer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        CommunityHealthVolunteer.delete()
        return Response({'message': 'CHV deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def chv_signup(request):
    serializer = CommunityHealthVolunteerSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hashed_password = make_password(password)
        CommunityHealthVolunteer = serializer.save(password=hashed_password)
        creator_id = request.data.get('created_by')
        if creator_id:
            creator = CustomUser.objects.filter(id=creator_id).first()
            if creator:
                CommunityHealthVolunteer.created_by = creator
                CommunityHealthVolunteer.save()
        return Response({'message': 'CHV registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def chv_logout(request):
    logout(request)
    return Response({'message': 'CHV logged out successfully'}, status=status.HTTP_200_OK)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def chv_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = CommunityHealthVolunteer.objects.filter(phone_number=phone_number).first()
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    elif user is None:
        return Response({'message': 'Invalid Crenditials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrAdmin])
def chv_detail(request, pk):
    try:
        chv = CommunityHealthVolunteer.objects.get(pk=pk)
    except CommunityHealthVolunteer.DoesNotExist:
        return Response({'message': 'CHV not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommunityHealthVolunteerSerializer(chv)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CommunityHealthVolunteerSerializer(chv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        chv.delete()
        return Response({'message': 'CHV deleted'}, status=status.HTTP_204_NO_CONTENT)







#tracking

class DailyLivingListView(APIView):
    def get(self, request):
        daily_living = DailyLiving.objects.all()
        serializer = DailyLivingSerializer(daily_living, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DailyLivingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DailyLivingDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            living = DailyLiving.objects.get(id=id)
            serializer = DailyLivingSerializer(living)
            return Response(serializer.data)
        except DailyLiving.DoesNotExist:
            return Response({"error": "Daily living activity not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            daily = DailyLiving.objects.get(id=id)
            serializer = DailyLivingSerializer(daily, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DailyLiving.DoesNotExist:
            return Response({"error": "Daily living activity not found"}, status=status.HTTP_404_NOT_FOUND) 
        
    def delete(self, request, id, format=None):
        try:
            daily = DailyLiving.objects.get(id=id)
            daily.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DailyLiving.DoesNotExist:
            return Response({"error": "Daily living activity not found"}, status=status.HTTP_404_NOT_FOUND)
class MovingAbilityListView(APIView):
    def get(self, request):
        moving = MovingAbility.objects.all()
        serializer = MovingAbilitySerializer(moving, many=True)
        total_count = moving.count()  
        response_data = {
            'total': total_count,  
            'data': serializer.data  
        }
        return Response(response_data)

    def post(self, request):
        serializer = MovingAbilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class MovingAbilityDetailview(APIView):
    def get(self, request, id, format=None):
        try:
            moving = MovingAbility.objects.get(id=id)
            serializer = MovingAbilitySerializer(moving)
            return Response(serializer.data)
        except MovingAbility.DoesNotExist:
            return Response("Moving Ability Activity does not exist", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            moving_ability = MovingAbility.objects.get(id=id)
            serializer = MovingAbilitySerializer(moving_ability, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)  
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except MovingAbility.DoesNotExist:
            return Response("Moving ability activity not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        try:
            moving = MovingAbility.objects.get(id=id)
            moving.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MovingAbility.DoesNotExist:
            return Response("Moving activity not found", status=status.HTTP_404_NOT_FOUND)   
class SelfCareListView(APIView):
    def get(self, request):
        self_care = SelfCareActivity.objects.all()
        serializer = SelfcareActivitySerializer(self_care, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SelfcareActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SelfcareDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            self = SelfCareActivity.objects.get(id=id)
            serializer = SelfcareActivitySerializer(self)
            return Response(serializer.data)
        except SelfCareActivity.DoesNotExist:
            return Response("Self Care Activity not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        try:
            Self_care = SelfCareActivity.objects.get(id=id)
            serializer = SelfcareActivitySerializer(Self_care, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except SelfCareActivity.DoesNotExist:
            return Response("Self Care activity not found", status=status.HTTP_404_NOT_FOUND)      
    def delete(self, request, id, format=None):
        try:
            self_care = SelfCareActivity.objects.get(id=id)
            self_care.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SelfCareActivity.DoesNotExist:
            return Response("Self Care activity not found", status=status.HTTP_404_NOT_FOUND)
class ParticipationListView(APIView):
    def get(self, request):
        participate = ParticipationInSocialLife.objects.all()
        serializer = ParticipationSerializer(participate, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParticipationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ParticipationDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            participate = ParticipationInSocialLife.objects.get(id=id)
            serializer = ParticipationSerializer(participate)
            return Response(serializer.data)
        except ParticipationInSocialLife.DoesNotExist:
            return Response("Participation not found", status=status.HTTP_404_NOT_FOUND)
    def put(self, request, id, format=None):
        try:
            participate = ParticipationInSocialLife.objects.get(id=id)
            serializer = ParticipationSerializer(participate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ParticipationInSocialLife.DoesNotExist:
            return Response("Participation not found", status=status.HTTP_404_NOT_FOUND)   
        
    def delete(self, request, id, format=None):
        try:
            participate = ParticipationInSocialLife.objects.get(id=id)
            participate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ParticipationInSocialLife.DoesNotExist:
            return Response("participation activity activity not found", status=status.HTTP_404_NOT_FOUND)    


#Child registration
        
class ChildDetailView(APIView):
    def get(self,request, id, format=None):
        try:
            child = ChildRegistration.objects.get(id=id)
            serializer = ChildSerializer(child)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ChildRegistration.DoesNotExist:
            return Response("Child not found", status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        child = ChildRegistration.objects.get(id=id)
        serializer = ChildSerializer(child, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
class ChildrenListView(APIView):
    def get(self, request):
        children = ChildRegistration.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            child = get_object_or_404(ChildRegistration, id=id)
            child.delete()
            return Response("Child deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except ChildRegistration.DoesNotExist:
            return Response("Child not found.", status=status.HTTP_404_NOT_FOUND)


#Guardian/parent

class GuardianListView(APIView):
    def get(self, request):
        guardians = Guardian.objects.all()
        serializer = GuardianListSerializer(guardians, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuardianDetailView(APIView):
    def get_object(self, id):
        try:
            return Guardian.objects.get(id=id)
        except Guardian.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        guardian = self.get_object(id)
        if guardian:
            serializer = GuardianSerializer(guardian)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": f"Guardian with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, id, format=None):
        guardian = self.get_object(id)
        if guardian:
            serializer = GuardianSerializer(guardian, data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"error": f"Guardian with id {id} does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        
class GuardianWithChildrenView(APIView):
    def get(self, request, guardian_id, format=None):
        try:
            guardian = Guardian.objects.get(id=guardian_id)
            serializer = GuardianSerializer(guardian)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Guardian.DoesNotExist:
            return Response("Guardian not found", status=status.HTTP_404_NOT_FOUND) 
         
   