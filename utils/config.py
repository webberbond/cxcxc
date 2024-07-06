from pydantic_settings import BaseSettings


class _Config(BaseSettings):
    BASE_URL: str
    DASHBOARD_EMAIL: str
    DASHBOARD_PASSWORD: str
    DASHBOARD_ERROR_EMAIL: str
    DASHBOARD_ERROR_PASSWORD: str

    class Config:
        env_file = ".env"


AppConfig = _Config()
