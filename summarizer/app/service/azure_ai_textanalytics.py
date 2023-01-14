from azure.ai.textanalytics import ExtractSummaryAction, TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from fastapi import HTTPException

from app import config


class AzureAITextAnalytics:
    def __init__(self):
        ta_credential = AzureKeyCredential(config.AZURE_API_KEY)
        self.text_analytics_client = TextAnalyticsClient(
            endpoint=config.AZURE_API_ENDPOINT, credential=ta_credential
        )

    def extractive_summarization(self, text):
        try:
            response = self.text_analytics_client.begin_analyze_actions(
                documents=[text],
                actions=[ExtractSummaryAction()],
                show_stats=True,
            ).result()
            for result in response:
                extract_summary_result = result[0]
                if extract_summary_result.is_error:
                    raise HTTPException(
                        status_code=extract_summary_result.code,
                        detail=extract_summary_result.message,
                    )
                return " ".join(
                    [sentence.text for sentence in extract_summary_result.sentences]
                )
        except Exception as e:
            print(e)
            return None
