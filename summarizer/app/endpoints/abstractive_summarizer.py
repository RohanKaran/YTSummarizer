from datetime import timedelta

from app.core import redis
from app.service.huggingface_inference import HuggingFaceInferenceService
from app.service.youtube_transcript import YouTubeTranscriptService
from fastapi import APIRouter

from summarizer.app.service.talkdoc import TalkDocService

api: APIRouter = APIRouter()


@api.get("/transcript/{yt_video_id}/")
async def summarize(yt_video_id: str):
    summary = await redis.hget(name=yt_video_id, key="abstractive")
    if summary:
        print("cached")
        return {"summary": summary}
    input_text = YouTubeTranscriptService.get_transcript(yt_video_id)
    try:
        talkdoc_service = TalkDocService()
        summary = talkdoc_service.get_short_summary(input_text)
    except Exception as e:
        print(e)
        huggingface_inference_service = HuggingFaceInferenceService()
        summary = huggingface_inference_service.summarize(input_text)
    await redis.hset(name=yt_video_id, key="abstractive", value=summary)
    await redis.expire(name=yt_video_id, time=timedelta(days=1))

    return {"summary": summary}
