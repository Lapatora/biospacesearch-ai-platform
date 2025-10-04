from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # App
    APP_NAME: str = "BioSpaceSearch AI Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database (using in-memory for demo)
    DATABASE_URL: str = "sqlite:///./nasa_ai_platform.db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # JWT
    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # OpenAI
    OPENAI_API_KEY: str = "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"
    
    # Pinecone
    PINECONE_API_KEY: str = "pcsk_2Su7CE_4pbgCQUcGrvTPixWhMZfgkgcpPJDJQjjomaxUC5UEaHsc3UTpcYee2TwurcZnwn"
    PINECONE_ENVIRONMENT: str = "us-west1-gcp"
    
    # File Storage
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 100 * 1024 * 1024  # 100MB
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

