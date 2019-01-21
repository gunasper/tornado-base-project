from handlers.auth_hello_world import AuthHelloWorldHandler

ROUTES = [                       
    (r"/v0/auth_hello_world/?$", AuthHelloWorldHandler),
]