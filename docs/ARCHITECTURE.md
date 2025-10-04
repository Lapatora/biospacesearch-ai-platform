# 🏗 Architecture - NASA Space Apps AI Platform

Документация архитектуры системы.

## 📐 Общая архитектура

```
┌─────────────────────────────────────────────────────────┐
│                    Client Browser                        │
│            (React + TypeScript + TailwindCSS)           │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP/HTTPS
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  Frontend Server                         │
│              (Static files / Nginx)                      │
└──────────────────────┬──────────────────────────────────┘
                       │ REST API
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  Backend API Server                      │
│              (FastAPI + Python 3.10+)                   │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Auth Service │  │ File Service │  │  AI Service  │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
└────┬──────────┬──────────┬──────────┬──────────────────┘
     │          │          │          │
     ▼          ▼          ▼          ▼
┌─────────┐ ┌──────┐ ┌─────────┐ ┌────────────┐
│PostgreSQL│ │Redis │ │ OpenAI  │ │  Pinecone  │
└─────────┘ └──────┘ └─────────┘ └────────────┘
```

---

## 🎯 Frontend Architecture

### Component Structure

```
frontend/
├── src/
│   ├── components/        # Переиспользуемые компоненты
│   │   ├── Layout.tsx    # Основной layout с сайдбаром
│   │   └── ...
│   │
│   ├── pages/            # Страницы приложения
│   │   ├── Dashboard.tsx # Главная страница с аналитикой
│   │   ├── FileManager.tsx # Управление файлами
│   │   ├── AIChat.tsx    # AI чат
│   │   ├── Profile.tsx   # Профиль пользователя
│   │   ├── FileEditor.tsx # Редактор файлов
│   │   ├── Login.tsx     # Авторизация
│   │   └── Register.tsx  # Регистрация
│   │
│   ├── services/         # API клиенты
│   │   ├── api.ts       # Базовый API клиент
│   │   ├── auth.ts      # Аутентификация
│   │   ├── files.ts     # Работа с файлами
│   │   └── chat.ts      # AI чат
│   │
│   ├── hooks/           # Custom React hooks
│   │   ├── useAuth.ts   # Хук для аутентификации
│   │   ├── useFiles.ts  # Хук для файлов
│   │   └── useChat.ts   # Хук для чата
│   │
│   ├── utils/           # Утилиты
│   │   ├── formatters.ts # Форматирование данных
│   │   └── validators.ts # Валидация
│   │
│   └── types/           # TypeScript типы
│       ├── user.ts
│       ├── file.ts
│       └── chat.ts
```

### State Management

- **Local State:** React useState для компонентов
- **Global State:** Context API для аутентификации
- **Server State:** React Query (можно добавить) для кэширования

### Key Features:

1. **Routing:** React Router v6
2. **Styling:** TailwindCSS + custom classes
3. **Icons:** Heroicons
4. **Charts:** Recharts
5. **Animations:** Framer Motion
6. **Forms:** Controlled components

---

## 🔧 Backend Architecture

### Project Structure

```
backend/
├── app/
│   ├── api/              # API endpoints
│   │   ├── auth.py      # Аутентификация
│   │   ├── files.py     # Файловые операции
│   │   ├── chat.py      # AI чат
│   │   └── users.py     # Профиль пользователя
│   │
│   ├── core/            # Основная конфигурация
│   │   ├── config.py    # Настройки приложения
│   │   ├── security.py  # JWT, хэширование
│   │   └── database.py  # Подключение к БД
│   │
│   ├── models/          # SQLAlchemy модели
│   │   ├── user.py
│   │   ├── file.py
│   │   └── chat.py
│   │
│   ├── services/        # Бизнес-логика
│   │   ├── ai_service.py      # OpenAI интеграция
│   │   ├── file_service.py    # Обработка файлов
│   │   ├── vector_service.py  # Pinecone векторный поиск
│   │   └── celery_tasks.py    # Фоновые задачи
│   │
│   └── utils/           # Утилиты
│       ├── file_parser.py # Парсинг PDF/DOCX
│       └── embeddings.py  # Генерация эмбеддингов
│
├── main.py             # Entry point FastAPI
└── requirements.txt    # Зависимости Python
```

### Layered Architecture

```
┌─────────────────────────────────────┐
│         API Layer (FastAPI)          │
│  - Request validation                │
│  - Response formatting               │
│  - Authentication                    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       Service Layer (Business Logic) │
│  - AI analysis                       │
│  - File processing                   │
│  - Vector search                     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Data Layer (Models + DB)        │
│  - SQLAlchemy ORM                    │
│  - Database operations               │
│  - Data validation                   │
└──────────────────────────────────────┘
```

---

## 💾 Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Files Table
```sql
CREATE TABLE files (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100),
    size BIGINT,
    path VARCHAR(512),
    tags TEXT[],
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Chat History Table
```sql
CREATE TABLE chat_messages (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    content TEXT NOT NULL,
    sender VARCHAR(10) NOT NULL, -- 'user' or 'ai'
    file_context UUID[],
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🤖 AI Integration Flow

### Document Analysis Pipeline

```
1. File Upload
   ↓
2. Extract Text
   - PDF → PyPDF2
   - DOCX → python-docx
   - CSV → pandas
   ↓
3. Chunk Text
   - Split into manageable chunks
   - Preserve context
   ↓
4. Generate Embeddings
   - OpenAI text-embedding-ada-002
   - 1536-dimensional vectors
   ↓
5. Store in Pinecone
   - Index by file_id
   - Store metadata
   ↓
6. AI Analysis
   - OpenAI GPT-4
   - Context from similar chunks
   ↓
7. Return Results
   - Summary
   - Key points
   - Insights
```

### Chat Flow

```
User Query
   ↓
1. Embed Query → OpenAI
   ↓
2. Search Similar Docs → Pinecone
   ↓
3. Retrieve Context → Top K matches
   ↓
4. Build Prompt
   - System message
   - Context from documents
   - User query
   ↓
5. Generate Response → GPT-4
   ↓
6. Stream/Return → Frontend
```

---

## 🔐 Security Architecture

### Authentication Flow

```
1. User Login
   ↓
2. Validate Credentials
   - Check email
   - Verify password hash (bcrypt)
   ↓
3. Generate JWT Token
   - Include user_id, email
   - Set expiration (24h)
   - Sign with secret key
   ↓
4. Return Token → Client
   ↓
5. Client stores in localStorage
   ↓
6. Include in subsequent requests
   - Authorization: Bearer <token>
```

### Security Layers

1. **Input Validation:** Pydantic models
2. **Authentication:** JWT tokens
3. **Authorization:** Role-based access (future)
4. **Rate Limiting:** Redis-based (future)
5. **File Validation:** Type, size checks
6. **SQL Injection:** SQLAlchemy ORM
7. **XSS Protection:** React escapes by default
8. **CORS:** Whitelist specific origins

---

## 🚀 Scalability Considerations

### Horizontal Scaling

```
┌───────────┐
│Load Balancer│
│  (Nginx)   │
└─────┬──────┘
      │
      ├──────┬──────┬──────┐
      │      │      │      │
    ┌─▼─┐  ┌─▼─┐  ┌─▼─┐  ┌─▼─┐
    │API│  │API│  │API│  │API│
    │ 1 │  │ 2 │  │ 3 │  │ 4 │
    └───┘  └───┘  └───┘  └───┘
```

### Caching Strategy

1. **Redis Cache:**
   - User sessions
   - Frequent queries
   - API responses (short TTL)

2. **CDN:**
   - Static assets
   - Frontend bundle

3. **Database Query Cache:**
   - SQLAlchemy query caching

### Background Jobs (Celery)

```python
# Task queue для:
- Длительный анализ файлов
- Генерация эмбеддингов
- Массовая обработка документов
- Email уведомления
```

---

## 📊 Monitoring & Logging

### Metrics to Track

1. **Performance:**
   - API response time
   - Database query time
   - File upload speed

2. **Usage:**
   - Active users
   - Files uploaded
   - AI queries

3. **Errors:**
   - 4xx/5xx responses
   - Failed AI requests
   - Database errors

### Logging Strategy

```python
# Structured logging
import logging

logger = logging.getLogger(__name__)

# Levels:
# - DEBUG: Development
# - INFO: General events
# - WARNING: Warnings
# - ERROR: Errors
# - CRITICAL: Critical issues
```

---

## 🔄 CI/CD Pipeline (Future)

```
Git Push
   ↓
GitHub Actions
   ↓
├─ Run Tests
├─ Lint Code
├─ Build Docker Images
└─ Deploy
   ├─ Staging → Auto
   └─ Production → Manual approval
```

---

## 📱 Future Enhancements

1. **Real-time Features:**
   - WebSocket for live chat
   - Collaborative document editing

2. **Advanced AI:**
   - Custom fine-tuned models
   - Multi-modal analysis (images + text)

3. **Mobile App:**
   - React Native
   - Native file access

4. **Analytics Dashboard:**
   - Advanced usage metrics
   - AI insights visualization

---

**Architecture документация обновляется по мере развития проекта.**

