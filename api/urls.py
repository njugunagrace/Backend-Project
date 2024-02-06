from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.urls import path,include
from .views import ParticipationListView , ParticipationDetailView , DailyLivingListView, DailyLivingDetailView, MovingAbilityListView , SelfCareListView, SelfcareDetailView, MovingAbilityDetailview
from rest_framework import permissions
from django.contrib import admin
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from api.views import  CommunityHealthVolunteerList , ChildrenListView , ChildDetailView, GuardianListView ,GuardianDetailView  , GuardianWithChildrenView

schema_view = get_schema_view(
    openapi.Info(
        title="Mwanga API",
        default_version='v1',
        description="API for identifying children with delayed milestones and tracking them",
        terms_of_service="https://www.mwanga.com/terms/",
        contact=openapi.Contact(email="qemerakirachix@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)
urlpatterns = [
    path('ngo/signup/', views.ngo_signup, name='ngo-signup'),
    path('ngo/logout/', views.ngo_logout, name='ngo-logout'),
    path('customusers/', views.CustomUserList.as_view(), name='customuser-list'),
    path('customusers/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
    path('healthworkers/', views.CommunityHealthVolunteerList.as_view(), name='healthworker-list'),
    path('healthworkers/<int:pk>/', views.chv_detail, name='healthworker-detail'),
    path('healthworker/signup/', views.chv_signup, name='healthworker-signup'),
    path('healthworker/logout/', views.chv_logout, name='healthworker-logout'),
    path('healthworker/login/', views.chv_login, name='healthworker-login'),
    path('ngo/login/', views.ngo_login, name='ngo-login'),
         
    path("daily_living/<int:id>/" , DailyLivingDetailView.as_view(), name="daily_detail_view"),
    path("daily_living/", DailyLivingListView.as_view(), name= "daily_list_view"),

    path("moving/" , MovingAbilityListView.as_view(), name="moving_list_view"),
    path("moving/<int:id>/", MovingAbilityDetailview.as_view(), name= " moving_detail_view"),

    path("self_care/" ,  SelfCareListView.as_view(), name ="self_care_list_view"),
    path("self_care/<int:id>/", SelfcareDetailView.as_view(), name= "self_care_detail_view"),

    path("participation/" , ParticipationListView.as_view(), name="participation_list_view"),
    path("participation/<int:id>/", ParticipationDetailView.as_view(), name="participation_detail_view"),

    path("children/", ChildrenListView.as_view(), name="child_list_view" ),
    path("children/<int:id>/", ChildDetailView.as_view(), name="children_detail_view"),

    path("guardians/",GuardianListView.as_view(),name="guardian_list_view"),
    path("guardians/<int:id>/",GuardianDetailView.as_view(),name = "guardian_detail_view"),
    path("guardian_children/<int:guardian_id>/", GuardianWithChildrenView.as_view(), name = "guardian_with_children"),



    path('document/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
