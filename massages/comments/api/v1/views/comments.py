from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from comments.api.v1.serializers.comments import CommentSerializer
from comments.models import Comment
from core.paginators.paginators import BasePaginator
from core.permissions.permissions import IsAuthenticatedOrReadOnly


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.filter(parent_comment__isnull=True).select_related('user').all()
    serializer_class = CommentSerializer
    pagination_class = BasePaginator
    ordering_fields = ['created_at', 'user__username', 'user__email']
    ordering = ['-created_at']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if not user:
            raise PermissionDenied("User must be authenticated")
        serializer.save(user=user)
