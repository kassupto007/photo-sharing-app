from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import views

router = DefaultRouter()
router.register('profiles', views.ProfileListAPIView, basename='profiles')
urlpatterns = [
    path('profiles/<pk>/', views.ProfileUpdateAPIView.as_view(), name='profile-update-view'),
]+router.urls
