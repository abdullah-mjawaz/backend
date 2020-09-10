from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
# from chat.consumers import ChatConsumer
# from chat.cache_cleaner import BackgroundTaskConsumer
# from notifications.consumers  import NotificationsConsumer
# from accounts.websocket_backend import JWTAuthMiddlewareStack
from channels.auth import AuthMiddlewareStack
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                # re_path('', ChatConsumer),
                # re_path('api/ws/chat/(?P<room_name>[^/]+)/', ChatConsumer),
                # re_path('api/ws/notifications/', NotificationsConsumer),
                # re_path('api/ws/notifications/(?P<room_name>[^/]+)/', NotificationsConsumer),
            ]
        )
    ),
    # 'channel': ChannelNameRouter({
    #     'background-tasks': BackgroundTaskConsumer,
    # })
})
