from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comment(models.Model):
    parent_comment = models.ForeignKey(
        'comments.Comment',
        on_delete=models.CASCADE,
        related_name='child_comments',
        null=True,
        blank=True
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
