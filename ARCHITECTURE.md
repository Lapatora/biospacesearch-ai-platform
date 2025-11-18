
#  **Architecture – NASA Space Apps AI Platform**

System architecture documentation.

---

##  **General Architecture**

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

##  **Frontend Architecture**

### Component Structure

```
frontend/
├── src/
│   ├── components/        # Reusable UI components
│   │   ├── Layout.tsx    # Main layout with sidebar
│   │   └── ...
│   │
│   ├── pages/            # Application pages
│   │   ├── Dashboard.tsx     # Main analytics page
│   │   ├── FileManager.tsx   # Files management
│   │   ├── AIChat.tsx        # AI Chat interface
│   │   ├── Profile.tsx       # User profile
│   │   ├── FileEditor.tsx    # File editor
│   │   ├── Login.tsx         # Login page
│   │   └── Register.tsx      # Registration page
│   │
│   ├── services/         # API clients
│   │   ├── api.ts       # Base API client
│   │   ├── auth.ts      # Authentication API
│   │   ├── files.ts     # File API
│   │   └── chat.ts      # Chat API
│   │
│   ├── hooks/           # Custom hooks
│   │   ├── useAuth.ts   # Authentication logic
│   │   ├── useFiles.ts  # File manager logic
│   │   └── useChat.ts   # Chat logic
│   │
│   ├── utils/           # Helper utils
│   │   ├── formatters.ts # Data formatting
│   │   └── validators.ts # Form validation
│   │
│   └── types/           # TypeScript types
│       ├── user.ts
│       ├── file.ts
│       └── chat.ts
```

### State Management

* **Local State:** `useState` for UI logic
* **Global State:** Context API for authentication
* **Server State:** *React Query* (optional) for caching and synchronization

### Key Features & Tools

1. **Routing:** React Router v6
2. **Styling:** TailwindCSS
3. **Icons:** Heroicons
4. **Charts:** Recharts
5. **Animations:** Framer Motion
6. **Forms:** Controlled components

---

##  **Backend Architecture**

### Project Structure

```
backend/
├── app/
│   ├── api/                      # API endpoints
│   │   ├── auth.py              # Authentication
│   │   ├── files.py             # File operations
│   │   ├── chat.py              # AI chat
│   │   └── users.py             # User profile
│   │
│   ├── core/                    # Core configuration
│   │   ├── config.py            # App config
│   │   ├── security.py          # JWT + hashing
│   │   └── database.py          # DB connection
│   │
│   ├── models/                  # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── file.py
│   │   └── chat.py
│   │
│   ├── services/                # Business logic
│   │   ├── ai_service.py        # OpenAI integration
│   │   ├── file_service.py      # File processing
│   │   ├── vector_service.py    # Pinecone vector store
│   │   └── celery_tasks.py      # Background async jobs
│   │
│   └── utils/                   # Utilities
│       ├── file_parser.py       # PDF/DOCX parsing
│       └── embeddings.py        # Embedding generator
│
├── main.py                      # FastAPI entrypoint
└── requirements.txt             # Python dependencies
```

### Layered Architecture

```
┌─────────────────────────────────────┐
│          API Layer (FastAPI)        │
│  - Request validation                │
│  - Response formatting               │
│  - Authentication                    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       Service Layer (Logic)         │
│  - AI analysis                       │
│  - File processing                   │
│  - Vector search                     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│        Data Layer (ORM + DB)         │
│  - SQLAlchemy models                  │
│  - CRUD operations                    │
│  - Data validation                    │
└──────────────────────────────────────┘
```

---

##  **Database Schema**

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

### Chat Messages Table

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

##  **AI Integration Flow**

### Document Analysis Pipeline

```
1. File Upload
   ↓
2. Text Extraction
   - PDF → PyPDF2
   - DOCX → python-docx
   - CSV → pandas
   ↓
3. Chunking
   ↓
4. Embedding Generation
   - OpenAI embedding model
   ↓
5. Pinecone Vector Storage
   ↓
6. AI Analysis using GPT model
   ↓
7. Return result (summary + insights)
```

### Chat Flow

```
User Query
   ↓
Embed Query → OpenAI
   ↓
Pinecone Similarity Search
   ↓
Context Retrieval
   ↓
Prompt Building
   ↓
GPT Response Generation
   ↓
Return/Stream to User
```

---

##  **Security Architecture**

### Authentication Flow

```
1. User Login
   ↓
2. Validate Credentials
   ↓
3. JWT Token Generation
   ↓
4. Return Token
   ↓
5. Store in localStorage
   ↓
6. Send with all requests
```

### Security Layers

| Area             | Technique            |
| ---------------- | -------------------- |
| Input Validation | Pydantic models      |
| Authentication   | JWT                  |
| Authorization    | Role-based (planned) |
| Sessions         | Redis (planned)      |
| File Safety      | Type/size validation |
| SQL Injection    | ORM                  |
| XSS              | React protection     |
| CORS             | Allowed origins      |

---

##  **Scalability**

### Horizontal Scaling

```
           ┌───────────┐
           │ Load Balancer (Nginx) │
           └─────┬──────┘
                 │
      ┌──────────┴──────────┬───────────┬───────────┐
      │          │          │           │
    ┌─▼─┐      ┌─▼─┐      ┌─▼─┐       ┌─▼─┐
    │API│      │API│      │API│       │API│
    │ 1 │      │ 2 │      │ 3 │       │ 4 │
    └───┘      └───┘      └───┘       └───┘
```

### Caching

* Redis (sessions, tokens, frequent responses)
* CDN (static frontend)
* DB caching (optional)

### Celery Tasks

* Long-running file processing
* Embedding generation
* Batch operations
* Notifications

---

##  Monitoring & Logging

### Key Metrics

1. API latency & throughput
2. Database performance
3. AI usage + success rates
4. Error monitoring

### Logging Levels

```python
DEBUG, INFO, WARNING, ERROR, CRITICAL
```

---

##  CI/CD Pipeline (Planned)

```
Git Push
   ↓
GitHub Actions
   ↓
├─ Tests
├─ Lint
├─ Docker Build
└─ Deployment
     ├─ Staging (auto)
     └─ Production (manual)
```

**Architecture documentation is updated as the project evolves.**
