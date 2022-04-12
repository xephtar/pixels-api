import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from canvas.models import CanvasData


class CanvasConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = 'canvas'

    @database_sync_to_async
    def create_chat(self, data):
        new_msg, is_created = CanvasData.objects.get_or_create(data=data)
        return new_msg

    @database_sync_to_async
    def get_data(self):
        history = CanvasData.objects.all()
        for data in history:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'canvas_data',
                    'data': data.data
                }
            )

    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.get_data()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'canvas_data',
                'data': json.dumps(data)
            }
        )

    # Receive message from room group
    async def canvas_data(self, event):
        data = event['data']
        new_msg = await self.create_chat(data)  # It is necessary to await creation of messages

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': new_msg.data
        }))

