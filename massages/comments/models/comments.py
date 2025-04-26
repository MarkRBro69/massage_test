from django.contrib.auth import get_user_model
from django.db import models

from comments.validators.comments import TextValidator
from core.constants.files import FileTypes
from core.validators.file_validators import FileExtensionValidator, FileSizeValidator

User = get_user_model()


class Comment(models.Model):
    parent_comment = models.ForeignKey(
        'comments.Comment',
        on_delete=models.CASCADE,
        related_name='child_comments',
        null=True,
        blank=True
    )
    text = models.TextField(validators=[TextValidator()])
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def get_upload_url(self, filename: str):
        return f"storage/comments/{self.user}/{filename}"

    file = models.FileField(
        upload_to=get_upload_url,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator((FileTypes.IMAGE, FileTypes.DOCUMENT)),
            FileSizeValidator(),
        ])
