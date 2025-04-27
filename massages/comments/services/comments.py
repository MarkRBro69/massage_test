from channels.layers import get_channel_layer
from django.core.cache import cache

from core.constants.constants import COMMENTS_NOTIFICATIONS_GROUP, CACHE_TTL


async def send_notifications():
    """
    Sends notifications to all connected clients when a new comment is created.

    This function uses Django Channels to send a message to all clients connected to
    the "comments_notifications" group, informing them that new comments are available.
    """
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
        COMMENTS_NOTIFICATIONS_GROUP,
        {
            'type': 'new_comment_created',
            'message': f'We have new comments'
        }
    )


def get_cache_key(page: str, ordering: str) -> str:
    """
    Generates a cache key based on the page and ordering parameters.

    Args:
        page (str): The page number.
        ordering (str): The ordering of comments (e.g., "-created_at").

    Returns:
        str: The generated cache key.
    """
    return f'comments_page_{page}_ordering_{ordering}'


def get_from_cache(page: str, ordering: str) -> str | None:
    """
    Retrieves data from the cache based on the page and ordering parameters.

    Args:
        page (str): The page number.
        ordering (str): The ordering of comments.

    Returns:
        str | None: Cached data if it exists, otherwise None.
    """
    cache_key = get_cache_key(page=page, ordering=ordering)
    return cache.get(cache_key)


def set_to_cache(page: str, ordering: str, data: str) -> None:
    """
    Sets data to the cache with the given page and ordering parameters.

    Args:
        page (str): The page number.
        ordering (str): The ordering of comments.
        data (str): The data to be cached.

    Returns:
        None
    """
    cache_key = get_cache_key(page=page, ordering=ordering)
    cache.set(cache_key, data, timeout=CACHE_TTL)
