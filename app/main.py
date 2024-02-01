from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware


from api.v1.routers import v1_router
from core.config import settings

app = FastAPI(
    title=settings.app.name,
    docs_url='/api/v1/openapi',
    openapi_url='/api/v1/openapi.json',
    redoc_url='/api/v1/redoc',
    default_response_class=ORJSONResponse,
)

app.include_router(v1_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)
