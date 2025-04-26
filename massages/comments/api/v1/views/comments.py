from rest_framework.viewsets import ModelViewSet

from comments.api.v1.serializers.comments import CommentSerializer
from comments.models import Comment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
