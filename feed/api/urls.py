from django.urls import path, include
from rest_framework.routers import DefaultRouter

from feed.api import views

router = DefaultRouter()
router.register('posts', views.PostAPIView, basename='posts')
# router.register('posts/<pk>', views.PostDetailsAPIView, basename='posts-details')
urlpatterns = router.urls
