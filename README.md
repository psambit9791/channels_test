# Django Channels Sample for a Simple Data Transmission Channel

This project aims to provide a much simpler example to understand the usage of Django Channels for using websockets in Django. This follows DjangoChannels version 2.1.7 and has major changes from version 1.

The project here provides 2 pages, a data source and a data sink. On the data source page, clicking button generates numbers and this numbers are shown on the data sink/destination page.

This channel is built using groups and consumers. We have 2 example async consumers shown here, AsyncJsonWebsocketConsumer and AsyncWebsocketConsumer.

