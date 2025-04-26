from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comments.api.v1.serializers.comments import CommentSerializer
from comments.models import Comment
from comments.producer.producer import send_comment_created_event
from comments.tasks import check_comments_text
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
            raise PermissionDenied('User must be authenticated')
        instance = serializer.save(user=user)

        check_comments_text.delay(instance.text)

        send_comment_created_event(
            comment_id=instance.id,
            text=instance.text,
            user_id=instance.user.id,
        )

    def list(self, request, *args, **kwargs):
        page = request.query_params.get('page', 1)
        ordering = request.query_params.get('ordering', '-created_at')
        cache_key = f'comments_page_{page}_ordering_{ordering}'

        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data, status=status.HTTP_200_OK)

        self.queryset = self.queryset.order_by(ordering)
        response = super().list(request, *args, **kwargs)

        cache.set(cache_key, response.data, timeout=30)
        return response
