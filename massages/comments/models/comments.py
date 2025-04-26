from django.db import models


class Comment(models.Model):
    parent_comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, related_name='child_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
