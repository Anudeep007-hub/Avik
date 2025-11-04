import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import call.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webrtc_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            call.routing.websocket_urlpatterns
        )
    ),
})
