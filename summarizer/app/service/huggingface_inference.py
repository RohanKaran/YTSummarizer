from typing import Optional

import requests
from fastapi import HTTPException
from starlette import status

from app import config


class HuggingFaceInferenceService:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {config.HUGGINGFACE_API_KEY}"}

    def summarize(
        self, text: str, model_name=config.HUGGINGFACE_MODEL_NAME
    ) -> Optional[str]:
        try:
            response = requests.post(
                f"{config.HUGGINGFACE_API_URI}/models/{model_name}",
                headers=self.headers,
                json={
                    "inputs": text,
                    "options": {
                        "use_cache": True,
                        "wait_for_model": True,
                    },
                },
            ).json()
            if isinstance(response, dict) and response.get("error"):
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail=response["error"],
                )
            return response[0]["summary_text"]
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="HuggingFace API is not available",
            )
