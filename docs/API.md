# 📚 API Documentation - NASA Space Apps AI Platform

Полная документация API endpoints для работы с платформой.

## 🔑 Аутентификация

Все защищенные endpoints требуют JWT токен в заголовке:
```
Authorization: Bearer <your-jwt-token>
```

---

## 🔐 Authentication Endpoints

### POST `/api/auth/register`
Регистрация нового пользователя

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### POST `/api/auth/login`
Вход в систему

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "securePassword123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### POST `/api/auth/refresh`
Обновление токена

**Headers:**
```
Authorization: Bearer <old-token>
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### GET `/api/auth/me`
Получение информации о текущем пользователе

**Response:**
```json
{
  "id": "1",
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## 📁 File Management Endpoints

### GET `/api/files`
Получить список всех файлов пользователя

**Response:**
```json
[
  {
    "id": "uuid-1",
    "name": "document.pdf",
    "type": "application/pdf",
    "size": 2400000,
    "uploadedAt": "2024-10-04T12:00:00Z",
    "tags": ["research", "nasa"]
  }
]
```

### POST `/api/files/upload`
Загрузить новый файл

**Request:**
- Content-Type: `multipart/form-data`
- Body: file (binary)

**Response:**
```json
{
  "id": "uuid-1",
  "name": "document.pdf",
  "message": "File uploaded successfully"
}
```

### GET `/api/files/{file_id}`
Получить информацию о файле

**Response:**
```json
{
  "id": "uuid-1",
  "name": "document.pdf",
  "type": "application/pdf",
  "size": 2400000,
  "uploadedAt": "2024-10-04T12:00:00Z",
  "tags": ["research"],
  "content_preview": "First 500 characters..."
}
```

### GET `/api/files/{file_id}/download`
Скачать файл

**Response:**
- Binary file data

### DELETE `/api/files/{file_id}`
Удалить файл

**Response:**
```json
{
  "message": "File deleted successfully"
}
```

### POST `/api/files/{file_id}/analyze`
Анализ файла с помощью AI

**Response:**
```json
{
  "file_id": "uuid-1",
  "analysis": {
    "summary": "Document summary...",
    "key_points": [
      "Point 1",
      "Point 2"
    ],
    "sentiment": "positive"
  }
}
```

---

## 💬 AI Chat Endpoints

### POST `/api/chat/message`
Отправить сообщение в AI чат

**Request Body:**
```json
{
  "content": "What are the main points in my research paper?",
  "file_context": ["uuid-1", "uuid-2"]
}
```

**Response:**
```json
{
  "id": "msg-1",
  "content": "Based on your research paper...",
  "sender": "ai",
  "timestamp": "2024-10-04T12:00:00Z"
}
```

### GET `/api/chat/history`
Получить историю чата

**Response:**
```json
{
  "messages": [
    {
      "id": "msg-1",
      "content": "Hello!",
      "sender": "user",
      "timestamp": "2024-10-04T12:00:00Z"
    },
    {
      "id": "msg-2",
      "content": "Hi! How can I help?",
      "sender": "ai",
      "timestamp": "2024-10-04T12:00:01Z"
    }
  ]
}
```

### DELETE `/api/chat/history`
Очистить историю чата

**Response:**
```json
{
  "message": "Chat history cleared"
}
```

### POST `/api/chat/analyze`
Комплексный анализ нескольких файлов

**Request Body:**
```json
{
  "file_ids": ["uuid-1", "uuid-2", "uuid-3"],
  "query": "Find common themes across these documents"
}
```

**Response:**
```json
{
  "query": "Find common themes...",
  "files_analyzed": 3,
  "insights": [
    "Common theme 1",
    "Common theme 2"
  ],
  "summary": "Overall analysis summary..."
}
```

---

## 👤 User Profile Endpoints

### GET `/api/users/profile`
Получить профиль и статистику пользователя

**Response:**
```json
{
  "id": "1",
  "name": "John Doe",
  "email": "john@example.com",
  "joined_date": "2024-10-01",
  "stats": {
    "total_files": 42,
    "total_storage_bytes": 2400000000,
    "ai_queries_count": 156,
    "recent_uploads": 8
  }
}
```

### PUT `/api/users/profile`
Обновить профиль пользователя

**Request Body:**
```json
{
  "name": "John Smith",
  "email": "john.smith@example.com"
}
```

**Response:**
```json
{
  "message": "Profile updated successfully",
  "name": "John Smith",
  "email": "john.smith@example.com"
}
```

---

## ⚠️ Error Responses

Все endpoints могут вернуть следующие ошибки:

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid or expired token"
}
```

### 403 Forbidden
```json
{
  "detail": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 413 Payload Too Large
```json
{
  "detail": "File too large. Maximum size is 100MB"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## 📝 Rate Limiting

- **Authentication endpoints:** 5 requests per minute
- **File upload:** 10 files per minute
- **AI chat:** 20 messages per minute
- **Other endpoints:** 100 requests per minute

---

## 🔄 Pagination

Endpoints с большим количеством данных поддерживают пагинацию:

**Query Parameters:**
- `page`: номер страницы (по умолчанию 1)
- `limit`: количество элементов на странице (по умолчанию 20, максимум 100)

**Example:**
```
GET /api/files?page=2&limit=50
```

---

## 🧪 Testing the API

### Using curl:

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"password123"}'

# Upload file
curl -X POST http://localhost:8000/api/files/upload \
  -H "Authorization: Bearer <token>" \
  -F "file=@document.pdf"

# Send chat message
curl -X POST http://localhost:8000/api/chat/message \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"content":"Analyze my documents"}'
```

### Using Postman:

1. Import collection from `/docs/postman_collection.json`
2. Set environment variable `base_url` to `http://localhost:8000`
3. Set `token` variable after login

---

## 📊 WebSocket Events (Future)

Для real-time уведомлений (в разработке):

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};
```

---

## 🔗 Interactive Documentation

Swagger UI доступен по адресу: `http://localhost:8000/docs`

ReDoc доступен по адресу: `http://localhost:8000/redoc`

---

**Happy coding! 🚀**

