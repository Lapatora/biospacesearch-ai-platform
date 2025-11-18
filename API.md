
#  **API Documentation - NASA Space Apps AI Platform**

Full documentation of API endpoints for working with the platform.

##  Authentication

All protected endpoints require a JWT token in the headers:

```
Authorization: Bearer <your-jwt-token>
```

---

## Authentication Endpoints

### **POST** `/api/auth/register`

Register a new user

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

---

### **POST** `/api/auth/login`

Log in to the system

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

---

### **POST** `/api/auth/refresh`

Refresh access token

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

---

### **GET** `/api/auth/me`

Get current user info

**Response:**

```json
{
  "id": "1",
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

## File Management Endpoints

### **GET** `/api/files`

Get list of all user files

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

---

### **POST** `/api/files/upload`

Upload new file

**Request:**

* Content-Type: `multipart/form-data`
* Body: file (binary)

**Response:**

```json
{
  "id": "uuid-1",
  "name": "document.pdf",
  "message": "File uploaded successfully"
}
```

---

### **GET** `/api/files/{file_id}`

Get file information

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

---

### **GET** `/api/files/{file_id}/download`

Download file
*Response contains binary data*

---

### **DELETE** `/api/files/{file_id}`

Delete file

**Response:**

```json
{
  "message": "File deleted successfully"
}
```

---

### **POST** `/api/files/{file_id}/analyze`

Analyze file using AI

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

## AI Chat Endpoints

### **POST** `/api/chat/message`

Send message to AI chat

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

---

### **GET** `/api/chat/history`

Get chat history

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

---

### **DELETE** `/api/chat/history`

Clear chat history

**Response:**

```json
{
  "message": "Chat history cleared"
}
```

---

### **POST** `/api/chat/analyze`

Perform complex multi-file analysis

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

## User Profile Endpoints

### **GET** `/api/users/profile`

Get user profile and statistics

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

---

### **PUT** `/api/users/profile`

Update profile

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

## Error Responses

All endpoints may return following errors:

| Status  | Description                |
| ------- | -------------------------- |
| **400** | Invalid request parameters |
| **401** | Invalid or expired token   |
| **403** | Insufficient permissions   |
| **404** | Resource not found         |
| **413** | File too large (max 100MB) |
| **500** | Internal server error      |

---

##  Rate Limiting

* **Auth endpoints:** 5 req/min
* **File upload:** 10 files/min
* **AI chat:** 20 messages/min
* **Others:** 100 requests/min

---

## Pagination

Endpoints with large datasets support pagination:

**Query params:**

* `page` — default: `1`
* `limit` — default: `20`, max: `100`

Example:

```
GET /api/files?page=2&limit=50
```

---

##  Testing the API

### Using `curl`:

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"password123"}'

# File upload
curl -X POST http://localhost:8000/api/files/upload \
  -H "Authorization: Bearer <token>" \
  -F "file=@document.pdf"

# Chat message
curl -X POST http://localhost:8000/api/chat/message \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"content":"Analyze my documents"}'
```

---

##  WebSocket Events (Future)

For real-time updates (coming soon):

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};
```

---

##  Interactive Documentation

* Swagger UI → `http://localhost:8000/docs`
* ReDoc → `http://localhost:8000/redoc`

---
