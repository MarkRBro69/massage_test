from rest_framework.viewsets import ModelViewSet

from comments.api.v1.serializers.comments import CommentSerializer
from comments.models import Comment
from core.paginators.paginators import BasePaginator


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.select_related('user').all()
    serializer_class = CommentSerializer
    pagination_class = BasePaginator
    ordering_fields = ['created_at', 'user__username', 'user__email']
    ordering = ['-created_at']
