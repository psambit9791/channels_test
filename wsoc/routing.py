from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from data_trans.consumers import DataConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter([
        path('transfer/', DataConsumer),
    ])
})