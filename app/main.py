from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

# Application packages
from app.Config import AppConf
from app.Http.middleware import ROUTES_MIDDLEWARE
from app.Api.V1 import api_router_v1

app = FastAPI(title=AppConf.APP_NAME, middleware=ROUTES_MIDDLEWARE)

# Register APIs
app.include_router(api_router_v1)

# Register static files
app.mount("/static", StaticFiles(directory="app/Storage/public"), name="static")

# Register startup event
@app.on_event("startup")
def startup_event():
    pass


@app.get("/")
async def read_home(request: Request):
    return 'It works!'