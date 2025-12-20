from app.core.config import settings
from app.core.database import engine
from app.core.database import Base
from app.api.v1.api import api_router
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

async def startup_tasks():
    print("NexoLetter: API Started")
    Base.metadata.create_all(bind=engine)

async def shutdown_tasks():
    print("NexoLetter: API Stopped")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_tasks()
    yield 
    await shutdown_tasks()

app = FastAPI(
    title = "NexoLetter API",
    description="AI Powered Newsletter SaaS Platform API",
    version="^1.0.0",
    lifespan = lifespan
)

if settings.ENVIRONMENT:
    origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["GET", "POST", "PUT", "PATCH"]
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred on the server.",
            "detail": str(exc)
        }
    )

app.include_router(api_router, prefix=settings.API_V1_STR)