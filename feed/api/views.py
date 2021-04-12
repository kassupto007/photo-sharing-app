from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feed.api.serializers import PostSerializer, CommentSerializer
from feed.models import Post, Comment


class PostAPIView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            serializer = self.get_serializer(instance=instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response({'message': 'You are not authorize to update this post'}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            self.perform_destroy(instance)
            return Response({'message': 'Post is deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'You are not authorize to delete this post'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get', 'post'], serializer_class=CommentSerializer)
    def comments(self, request, pk):
        if self.request.method == 'GET':
            comment = Comment.objects.filter(post_id=pk)
            return Response(CommentSerializer(comment, many=True).data)
        elif self.request.method == 'POST':
            comment = Comment.objects.create(owner=self.request.user, post_id=pk,
                                             comment=self.request.POST.get('comment'))
            return Response(CommentSerializer(comment).data)

    @action(detail=True, methods=['get', 'put', 'delete'], url_path='comments/(?P<pk2>[^/.]+)',
            serializer_class=CommentSerializer)
    def comment(self, request, pk, pk2):
        if self.request.method == 'GET':
            comment = Comment.objects.filter(post_id=pk, id=pk2).first()
            return Response(CommentSerializer(comment, many=False).data)
        elif self.request.method == 'PUT':
            try:
                comment = Comment.objects.get(post_id=pk, id=pk2)
                if comment.owner == self.request.user:
                    comment.comment = self.request.POST.get('comment')
                    comment.save()
                    return Response(CommentSerializer(comment).data)
                else:
                    return Response({'message': 'You are not authorize to update this comment'},
                                    status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'message': 'No comment found'}, status=status.HTTP_404_NOT_FOUND)
        elif self.request.method == 'DELETE':
            try:
                comment = Comment.objects.get(post_id=pk, id=pk2)
                if comment.owner == self.request.user:
                    comment.delete()
                    return Response({'message': 'Comment is deleted'}, status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'You are not authorize to delete this comment'},
                                    status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'message': 'No comment found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Bad Request'}, status.HTTP_400_BAD_REQUEST)
