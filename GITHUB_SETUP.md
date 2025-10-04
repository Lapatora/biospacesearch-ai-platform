# 📚 Настройка GitHub для BioSpaceSearch

## 1. Создание репозитория

1. Перейдите на [GitHub.com](https://github.com)
2. Нажмите "New repository"
3. Название: `biospacesearch-ai-platform`
4. Описание: `AI Platform for Space Research`
5. Выберите "Public" или "Private"
6. НЕ добавляйте README, .gitignore, лицензию (уже есть)
7. Нажмите "Create repository"

## 2. Загрузка проекта

```bash
# Инициализация Git (если еще не сделано)
git init

# Добавление файлов
git add .

# Первый коммит
git commit -m "Initial commit: BioSpaceSearch AI Platform"

# Подключение к GitHub
git remote add origin https://github.com/YOUR_USERNAME/biospacesearch-ai-platform.git

# Загрузка на GitHub
git push -u origin main
```

## 3. Настройка .gitignore

Убедитесь, что в `.gitignore` есть:
```
# Dependencies
node_modules/
venv/
__pycache__/

# Environment
.env
.env.local

# Uploads
uploads/*.txt
uploads/*.pdf
uploads/*.docx

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

## 4. Описание репозитория

Добавьте в описание:
```
🚀 AI Platform for Space Research

Features:
- AI Chat in Russian
- File Upload & Analysis
- User Profiles
- Team Collaboration
- Space Research Tools

Tech: React + FastAPI + OpenRouter AI
```

## 5. Теги и релизы

```bash
# Создание тега
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0

# Создание релиза на GitHub
# Перейдите в Releases → Create a new release
# Выберите тег v1.0.0
# Добавьте описание изменений
```

## 6. Настройка Pages (опционально)

1. Перейдите в Settings → Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)
5. Сохраните

## 7. Коллабораторы

1. Settings → Manage access
2. Invite a collaborator
3. Добавьте email или username

## Готово! 🎉

Ваш проект теперь на GitHub и готов к совместной работе!