from fastapi import APIRouter, Depends, HTTPException
from app.api.auth import oauth2_scheme, fake_users_db
from app.core.config import settings
from datetime import datetime
from jose import JWTError
from jose import jwt

router = APIRouter()

# Мок-история чата
chat_history = {}

# Модели (если ещё не определены)
from pydantic import BaseModel
from typing import List

class UserStats(BaseModel):
    total_files: int
    total_storage_bytes: int
    ai_queries_count: int
    recent_uploads: int

class UserProfile(BaseModel):
    email: str
    full_name: str
    joined_at: str
    stats: UserStats

@router.get("/profile", response_model=UserProfile)
async def get_user_profile():
    """Get user profile and statistics"""
    try:
        # Получаем последнего зарегистрированного пользователя
        if not fake_users_db:
            # Если нет пользователей, создаем тестового
            email = "user@example.com"
            fake_users_db[email] = {
                "email": email,
                "name": "Test User",
                "hashed_password": "test",
                "joined_at": datetime.now().isoformat()
            }
        else:
            # Берем последнего зарегистрированного пользователя
            email = list(fake_users_db.keys())[-1]
        
        user = fake_users_db[email]
        
        # Получаем статистику пользователя (mock данные)
        stats = UserStats(
            total_files=len(user.get("files", [])),
            total_storage_bytes=1840000000,  # 1.84 GB
            ai_queries_count=47,  # количество AI запросов
            recent_uploads=3  # последние загрузки
        )
        
        profile = UserProfile(
            email=user["email"],
            full_name=user.get("name", user.get("full_name", "Unknown User")),
            joined_at=user.get("joined_at", datetime.now().isoformat()),
            stats=stats
        )
        
        return profile
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.put("/profile")
async def update_user_profile(
    full_name: str = None,
    token: str = Depends(oauth2_scheme)
):
    """Update user profile"""
    try:
        # Декодируем токен для получения email пользователя
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None or email not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Обновляем данные пользователя
        if full_name:
            fake_users_db[email]["full_name"] = full_name
        
        return {
            "message": "Profile updated successfully",
            "email": email,
            "full_name": fake_users_db[email]["full_name"]
        }
        
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
