from django.http import Http404
from rest_framework import viewsets, mixins, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import ProfileSerializer
from users.models import Profile


class ProfileListAPIView(viewsets.GenericViewSet,
                         mixins.ListModelMixin, ):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        user = self.queryset.filter(pk=self.kwargs['pk']).first()
        if user == self.request.user:
            return self.update(request, *args, **kwargs)
        return Response({'message': 'You are not authorized to update this user'}, status=status.HTTP_400_BAD_REQUEST)

