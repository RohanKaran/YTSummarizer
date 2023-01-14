from pydantic import AnyHttpUrl, BaseSettings


class Config(BaseSettings):
    API_KEY: str = "secret"
    # Huggingface API
    HUGGINGFACE_API_URI: AnyHttpUrl = "https://api-inference.huggingface.co"
    HUGGINGFACE_MODEL_NAME: str = "google/pegasus-xsum"
    HUGGINGFACE_API_KEY: str
    # Azure config
    AZURE_API_KEY: str
    AZURE_API_ENDPOINT: str
    # Redis config
    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Config()
