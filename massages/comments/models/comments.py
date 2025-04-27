from django.contrib.auth import get_user_model
from django.db import models

from comments.validators.comments import TextValidator
from core.constants.files import FileTypes
from core.utils.files import is_image, is_gif, get_file_extension
from core.validators.file_validators import FileExtensionValidator, FileSizeValidator
from comments.tasks import process_image_task, process_gif_task

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', blank=True)

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file:
            if is_image(self.file):
                process_image_task.delay(self.file.path)

            if is_gif(self.file):
                process_gif_task.delay(self.file.path)
