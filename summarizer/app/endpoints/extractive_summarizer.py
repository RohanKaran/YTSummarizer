from datetime import timedelta

from app.core import redis
from app.service.azure_ai_textanalytics import AzureAITextAnalytics
from app.service.talkdoc import TalkDocService
from app.service.youtube_transcript import YouTubeTranscriptService
from fastapi import APIRouter

api: APIRouter = APIRouter()


@api.get("/transcript/{yt_video_id}/")
async def summarize(yt_video_id: str):
    summary = await redis.hget(name=yt_video_id, key="extractive")
    if summary:
        print("cached")
        return {"summary": summary}
    input_text = YouTubeTranscriptService.get_transcript(yt_video_id)

    try:
        talkdoc_service = TalkDocService()
        summary = talkdoc_service.get_long_summary(input_text)
    except Exception as e:
        print(e)
        azure_ai_textanalytics = AzureAITextAnalytics()
        summary = azure_ai_textanalytics.extractive_summarization(input_text)
    await redis.hset(name=yt_video_id, key="extractive", value=summary)
    await redis.expire(name=yt_video_id, time=timedelta(days=1))

    return {"summary": summary}
