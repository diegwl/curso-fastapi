from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://diegwl:Diego02071004castan@localhost:5432/faculdade"

    class Config:
        case_sensitive = True

settings: Settings = Settings()
