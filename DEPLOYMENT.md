# 🚀 Deployment Guide - NASA Space Apps AI Platform

Полное руководство по развертыванию проекта на локальном компьютере и в production.

## 📋 Предварительные требования

### Необходимое ПО:
- **Node.js** (v18+) и npm
- **Python** (3.10+)
- **PostgreSQL** (14+)
- **Redis** (6+)
- **Git**

### API Keys (опционально для полной функциональности):
- OpenAI API key
- Pinecone API key

---

## 🏃 Быстрый старт (локальная разработка)

### 1. Клонирование репозитория

```bash
cd nasa-space-apps-ai-platform
```

### 2. Настройка переменных окружения

```bash
cp .env.example .env
```

Отредактируйте `.env` файл и добавьте ваши значения:

```env
# Минимальная конфигурация для локальной разработки
DATABASE_URL=postgresql://user:password@localhost:5432/nasa_ai_platform
REDIS_URL=redis://localhost:6379
JWT_SECRET_KEY=your-random-secret-key-at-least-32-characters
OPENAI_API_KEY=sk-your-openai-key  # Опционально
```

### 3. Установка зависимостей

#### Frontend:
```bash
cd frontend
npm install
```

#### Backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Настройка базы данных

```bash
# Создайте PostgreSQL базу данных
createdb nasa_ai_platform

# Запустите миграции (если есть)
cd backend
alembic upgrade head
```

### 5. Запуск сервисов

#### Терминал 1 - Backend:
```bash
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Терминал 2 - Frontend:
```bash
cd frontend
npm start
```

#### Терминал 3 - Redis (если не запущен как сервис):
```bash
redis-server
```

### 6. Доступ к приложению

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

---

## 🏭 Production Deployment

### Option 1: Docker (рекомендуется)

Создайте `docker-compose.yml`:

```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    environment:
      - REACT_APP_API_URL=http://backend:8000
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/nasa_ai_platform
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
    volumes:
      - uploads:/app/uploads

  db:
    image: postgres:14
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=nasa_ai_platform
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:6
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
  uploads:
```

Запуск:
```bash
docker-compose up -d
```

### Option 2: Cloud Deployment

#### Frontend (Vercel/Netlify):

```bash
cd frontend
npm run build
# Deploy build/ folder to Vercel or Netlify
```

#### Backend (Heroku/Railway/DigitalOcean):

```bash
# Heroku example
heroku create nasa-ai-platform-backend
git push heroku main

# Set environment variables
heroku config:set OPENAI_API_KEY=your-key
heroku config:set DATABASE_URL=your-postgres-url
```

---

## 🔧 Настройка для NASA Space Apps Challenge

### 1. Интеграция OpenAI

Добавьте в `.env`:
```env
OPENAI_API_KEY=sk-your-key
```

В `backend/app/services/ai_service.py` создайте:

```python
import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def analyze_document(text: str):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a NASA data analyst."},
            {"role": "user", "content": f"Analyze this document: {text}"}
        ]
    )
    return response.choices[0].message.content
```

### 2. Векторный поиск с Pinecone

```python
import pinecone
from app.core.config import settings

pinecone.init(
    api_key=settings.PINECONE_API_KEY,
    environment=settings.PINECONE_ENVIRONMENT
)

index = pinecone.Index("nasa-documents")

async def store_document_embedding(doc_id: str, text: str):
    # Generate embedding with OpenAI
    embedding = await openai.Embedding.acreate(
        input=text,
        model="text-embedding-ada-002"
    )
    
    # Store in Pinecone
    index.upsert([(doc_id, embedding["data"][0]["embedding"])])
```

---

## 🧪 Тестирование

### Frontend:
```bash
cd frontend
npm test
```

### Backend:
```bash
cd backend
pytest
```

---

## 📊 Мониторинг и логирование

### Production логи:

```bash
# Backend logs
tail -f backend/logs/app.log

# PostgreSQL logs
tail -f /var/log/postgresql/postgresql.log
```

---

## 🔐 Безопасность

### Чеклист для production:

- [ ] Изменить `JWT_SECRET_KEY` на случайную строку (32+ символа)
- [ ] Включить HTTPS (SSL сертификат)
- [ ] Настроить CORS только для вашего домена
- [ ] Ограничить размер загружаемых файлов
- [ ] Включить rate limiting
- [ ] Настроить backup базы данных
- [ ] Использовать environment variables для всех секретов
- [ ] Включить логирование доступа

---

## 🚨 Troubleshooting

### Frontend не запускается:
```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

### Backend ошибки:
```bash
# Проверьте логи
tail -f backend/logs/error.log

# Проверьте соединение с БД
psql -U user -d nasa_ai_platform -c "SELECT 1;"
```

### Проблемы с Redis:
```bash
# Проверьте статус
redis-cli ping
# Должен вернуть: PONG
```

---

## 📞 Support

Для вопросов по NASA Space Apps Challenge:
- Email: support@nasa-ai-platform.com
- GitHub Issues: [ссылка]

---

**Удачи на NASA Space Apps Challenge! 🚀**

