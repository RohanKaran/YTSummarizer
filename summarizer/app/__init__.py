import aioredis as aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core import config
from .endpoints import api


def create_app():

    app = FastAPI(
        title="YTSummarizer API",
        version="1.0.0",
        description="A simple API for summarizing YouTube videos"
    )

    register_extensions(app)

    app.include_router(api, prefix="/api")  # pyright: reportGeneralTypeIssues=false

    return app


def register_extensions(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
