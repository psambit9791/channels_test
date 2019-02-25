import asyncio
import json
from django.contrib.auth import get_user_model
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class DataConsumer(JsonWebsocketConsumer):

    def connect(self):
        print(self.channel_layer)
        async_to_sync(self.channel_layer.group_add)(
            "dtrans",
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            "dtrans",
            self.channel_name
        )

    def receive(self, text_data):
        self.receive_json(self.decode_json(text_data))

    def receive_json(self, data=None):
        # Send message to room group
        print('Type of content:', type(data))
        print('Content:', data)
        # print('\n\n', text_data, '\n\n')
        async_to_sync(self.channel_layer.group_send)(
            "dtrans",
            {
                "type": "parse.message",
                "text": data
            }
        )

    def parse_message(self, event):
        self.send_json(event['text'])
