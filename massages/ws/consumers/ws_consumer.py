import json
from channels.generic.websocket import AsyncWebsocketConsumer

from core.constants.constants import COMMENTS_NOTIFICATIONS_GROUP


class CommentsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = COMMENTS_NOTIFICATIONS_GROUP

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        pass

    async def new_comment_created(self, event):
        print('new comments started')
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
