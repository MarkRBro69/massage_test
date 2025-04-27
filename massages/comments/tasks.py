import asyncio

from celery import shared_task

from comments.services.comments import send_notifications


@shared_task
def check_comments_text(text: str) -> bool:
    if isinstance(text, str):
        return True

    return False


@shared_task
def send_notifications_task() -> None:
    asyncio.run(send_notifications())
