from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Schedule Service"

    debug: bool = True

settings = Settings()