import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.startup import router as router_startup
from api.shutdown import router as router_shutdown
from api.base import router as router_base
from api.user import router as router_user
from api.role import router as router_role

from api.auth import router as router_auth
from settings import get_settings



app = FastAPI(
    title="Auth Demo",
    description="",
    version="1",
    debug= get_settings().api_debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_startup)
app.include_router(router_shutdown)
app.include_router(router_base)
app.include_router(router_user)
app.include_router(router_role)

app.include_router(router_auth)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")