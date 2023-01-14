from fastapi import HTTPException
from starlette import status
from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriptService:
    @staticmethod
    def get_transcript(video_id):
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No transcript found for the given video id",
            )

        english_transcript = None
        for transcript in transcript_list:
            if transcript.language_code in ["en", "en-US", "en-UK"]:
                english_transcript = transcript.fetch()
                break

        if not english_transcript:
            for transcript in transcript_list:
                english_transcript = transcript.translate("en").fetch()
                break

        result = ""
        for transcript in english_transcript:
            result += (
                transcript["text"]
                .replace("\n", " ")
                .replace("[Music]", "")
                .replace("[Applause]", "")
                .replace("[Laughter]", "")
                + " "
            )
        result = result.replace("  ", " ").strip()
        return result
