from typing import NamedTuple

COMMENTS_NOTIFICATIONS_GROUP = 'comments_notifications'

CACHE_TTL = 15  # seconds


class ImageSize(NamedTuple):
    width: int
    height: int


MAX_IMAGE_SIZE = ImageSize(width=320, height=240)  # pixels
