from handlers.auth_hello_world import AuthHelloWorldHandler
from handlers.server_status import StatusHandler

ROUTES = [                       
    (r"/v0/auth_hello_world/?$", AuthHelloWorldHandler),
    (r"/v0/server_status/?$", StatusHandler),
]