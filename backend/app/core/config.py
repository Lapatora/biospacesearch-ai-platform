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
    
    # OpenAI (fallback)
    OPENAI_API_KEY: str = "your-openai-api-key-here"
    
    # OpenRouter (primary) - FREE API
    OPENROUTER_API_KEY: str = "your-openrouter-api-key-here"
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"
    OPENROUTER_MODEL: str = "google/gemma-2-9b-it:free"
    
    # Pinecone
    PINECONE_API_KEY: str = "your-pinecone-api-key-here"
    PINECONE_ENVIRONMENT: str = "us-west1-gcp"
    
    # File Storage
    UPLOAD_DIR: str = "./uploads"
    MAX_FILE_SIZE: int = 100 * 1024 * 1024  # 100MB
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

