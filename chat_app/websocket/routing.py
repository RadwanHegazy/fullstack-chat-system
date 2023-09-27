from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/connect/", consumers.OnlineOffline.as_asgi()),
    path("ws/chat/<str:chatuuid>/", consumers.ChatConsumer.as_asgi()),
]