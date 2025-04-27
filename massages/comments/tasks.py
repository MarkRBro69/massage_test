import asyncio

from celery import shared_task

from comments.services.comments import send_notifications
from core.utils.files import resize_image, resize_gif


@shared_task
def check_comments_text(text: str) -> bool:
    if isinstance(text, str):
        return True

    return False


@shared_task
def send_notifications_task() -> None:
    asyncio.run(send_notifications())


@shared_task
def process_image_task(file_path):
    resize_image(file_path=file_path)


@shared_task
def process_gif_task(file_path):
    resize_gif(file_path=file_path)
