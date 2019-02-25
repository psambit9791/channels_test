import asyncio
import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import JsonWebsocketConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync


class DataConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "dtrans",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "dtrans",
            self.channel_name
        )

    async def receive(self, text_data):
        await self.receive_json(await self.decode_json(text_data))

    async def receive_json(self, data=None):
        # Send message to room group
        # print('\n\n', text_data, '\n\n')
        await self.channel_layer.group_send(
            "dtrans",
            {
                "type": "parse.message",
                "text": data
            }
        )

    async def parse_message(self, event):
        await self.send_json(event['text'])
