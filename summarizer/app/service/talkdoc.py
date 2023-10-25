import requests


class TalkDocService:
    def __init__(self):
        self.host = "https://tmapiprod.talkingmart.com/api/talkdoc/summary"

    def get_short_summary(self, text):
        response = requests.post(
            self.host,
            json={
                "prompt": f"Generate a short summary of the following YouTube video:\n{text[:5000]}",
            },
        )
        return response.json()["summary"]

    def get_long_summary(self, text):
        response = requests.post(
            self.host,
            json={
                "prompt": f"Generate a detailed summary of the following YouTube video:\n{text[:5000]}",
            },
        )
        return response.json()["summary"]
