from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
import time 

origins = [
    "http://127.0.0.1:8080",
]

trusted_hosts = [
    'example.com', 
    '*.example.com',
    # '127.0.0.1',
]

from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import base64
import binascii

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        # TODO
        # 1. Retrive Authorization: Bearer token
        # 2. Validate jwt Bearer token
        # 3. return Not authenticated or next request

        if "Authorization" not in request.headers:    
            raise AuthenticationError('Not authenticated')

        auth = request.headers["Authorization"]
        try:
            # Validate jwt token here
            scheme, credentials = auth.split()
            if scheme != 'bearer':
                raise AuthenticationError('Require bearer token')
        except:
            raise AuthenticationError('Invalid bearer auth credentials')

        # return AuthCredentials(["authenticated"])


class AddProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_value='Example'):
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


class LanguagueMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_value='en'):
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Content-Language"] = self.header_value
        return response

        
ROUTES_MIDDLEWARE = [
    # Middleware(HTTPSRedirectMiddleware),
    Middleware(AddProcessTimeHeaderMiddleware),
    Middleware(LanguagueMiddleware),
    Middleware(GZipMiddleware, minimum_size=1000),
    Middleware(CORSMiddleware, 
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
    # Middleware(TrustedHostMiddleware, allowed_hosts=trusted_hosts),
    # Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]