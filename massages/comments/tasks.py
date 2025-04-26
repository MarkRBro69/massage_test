from celery import shared_task


@shared_task
def check_comments_text(text: str) -> bool:
    if isinstance(text, str):
        return True

    return False
