from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='profile-update-view')

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'email', 'image', 'bio', 'url']
        read_only_fields = ('id', 'username')
