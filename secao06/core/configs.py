from typing import List, ClassVar

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://diegwl:Diego02071004castan@localhost:5432/faculdade"
    DBBaseModel: ClassVar = declarative_base()
    
    JWT_SECRET: str = 'vU8YRBp-hTYV6-o92F4DUOVo9fQooWpYfj1xFAFKxrI'
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True
        
settings: Settings = Settings()    