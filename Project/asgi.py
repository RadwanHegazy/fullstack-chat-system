import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from chat_app.websocket.routing import websocket_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django_asgi_app = get_asgi_application()

import chat_app.websocket.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)