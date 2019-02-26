from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from data_trans.consumers import DataConsumer, WSConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter([
        path('json_transfer/', DataConsumer),
        path('ws_transfer/', WSConsumer),
    ])
})