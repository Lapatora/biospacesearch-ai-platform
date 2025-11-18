
---

# Quick Start Guide / Краткое руководство по запуску

---

## Requirements / Требования

```bash
Node.js 18+
Python 3.10+
```

---

## Step 1: Frontend / Шаг 1: Фронтенд

**EN**

```bash
cd frontend
npm install
npm start
```

Frontend will be available at:
`http://localhost:3000`

**RU**

```bash
cd frontend
npm install
npm start
```

Фронтенд откроется по адресу:
`http://localhost:3000`

---

## Step 2: Backend / Шаг 2: Бэкенд

Open a new terminal window.
Откройте новое окно терминала.

**EN**

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Backend will run at:
`http://localhost:8000`

**RU**

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Бэкенд будет доступен по адресу:
`http://localhost:8000`

---

## Step 3: Login / Шаг 3: Вход в систему

**EN**

1. Open `http://localhost:3000`
2. Click "Create an account"
3. Register using any email and password

**RU**

1. Откройте `http://localhost:3000`
2. Нажмите кнопку "Create an account"
3. Зарегистрируйтесь, используя любой email и пароль

---
