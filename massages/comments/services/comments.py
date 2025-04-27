from channels.layers import get_channel_layer
from django.core.cache import cache

from core.constants.constants import COMMENTS_NOTIFICATIONS_GROUP, CACHE_TTL


async def send_notifications():
    print('send notifications started')
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
        COMMENTS_NOTIFICATIONS_GROUP,
        {
            'type': 'new_comment_created',
            'message': f'We have new comments'
        }
    )


def get_cache_key(page: str, ordering: str) -> str:
    return f'comments_page_{page}_ordering_{ordering}'


def get_from_cache(page: str, ordering: str) -> str | None:
    cache_key = get_cache_key(page=page, ordering=ordering)
    return cache.get(cache_key)


def set_to_cache(page: str, ordering: str, data: str) -> None:
    cache_key = get_cache_key(page=page, ordering=ordering)
    cache.set(cache_key, data, timeout=CACHE_TTL)
