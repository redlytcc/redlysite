from channels.routing import route
from redweb import consumers

channel_routing = [
	route('websocket.connect', 		consumers.ws_add,			path=r'^/redly/$'),
	route('websocket.receive', 		consumers.ws_message,		path=r'^/redly/$'),
	route('websocket.disconnect',	consumers.ws_disconnect, 	path=r'^/redly/$'),
]
