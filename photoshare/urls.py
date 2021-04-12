"""photoshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from feed.api import views
from feed.api.views import PostAPIView
from users.api.views import ProfileListAPIView, ProfileUpdateAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
r1=DefaultRouter()
r1.register('posts', PostAPIView, basename='posts')
r1.register('profiles', ProfileListAPIView, basename='profiles')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),
    path('', include('users.urls')),
    path('api/', include(r1.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/profiles/<pk>/', ProfileUpdateAPIView.as_view(), name='profile-update-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # include media files into routes
