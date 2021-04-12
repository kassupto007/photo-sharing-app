from rest_framework import serializers

from feed.models import Post, Comment
from users.api.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'comment', 'comment_date')
        read_only_fields = ('post', 'owner', 'comment_date')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    owner = ProfileSerializer(many=False, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail')
    class Meta:
        model = Post
        fields = ['id', 'owner', 'picture', 'date_posted', 'comments', 'description', 'url']
        read_only_fields = ('owner', 'comments')
