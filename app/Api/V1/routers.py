from fastapi import APIRouter
from .endpoints import setting, item

api_router_v1 = APIRouter(prefix="/v1")
api_router_v1.include_router(setting.router, prefix="/settings", tags=["setting"])
api_router_v1.include_router(item.router, prefix="/items", tags=["item"])

