from fastapi import APIRouter

from .abstractive_summarizer import api as abstractive_summarizer_api
from .extractive_summarizer import api as extractive_summarizer_api

api: APIRouter = APIRouter()

api.include_router(
    extractive_summarizer_api,
    tags=["Extractive Summarizer"],
    prefix="/summarizer-extractive",
)
api.include_router(
    abstractive_summarizer_api,
    tags=["Abstractive Summarizer"],
    prefix="/summarizer-abstractive",
)
