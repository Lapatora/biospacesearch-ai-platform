
# BioSpaceSearch AI Platform

AI platform for space research — a modern web application for analyzing space-related data using artificial intelligence.
About:
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 58 PM" src="https://github.com/user-attachments/assets/f6cae421-ecce-479b-a370-adf502ef26d4" />





---

## Features

* AI Chat — interact with the AI assistant
* File Management — upload and analyze documents
* User Profile — personalized settings
* Team Collaboration — work together on shared projects
* Data Analysis — AI automatically analyzes uploaded files

---

## Quick Start

### Requirements

```
Node.js 18+
Python 3.8+
Git
```

### Installation & Launch

Clone the repository:

```bash
git clone <your-repo-url>
cd nasa-space-apps-ai-platform
```

Run the project:

```bash
./start.sh
```

Open in browser:

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API: [http://localhost:8000](http://localhost:8000)
* API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Project Structure

```
├── frontend/          # React application
├── backend/           # FastAPI server
├── start.sh           # Startup script
└── README.md          # Documentation
```

---

## Technologies

### Frontend

* React 18 + TypeScript
* Tailwind CSS
* React Router

### Backend

* FastAPI (Python)
* OpenRouter AI API
* SQLite database

---

## Usage

1. Sign up — create a new account
2. File Upload — add documents for AI processing
3. AI Chat — discuss space-related topics with AI
4. Data Analysis — AI will analyze your uploaded files

---

## Configuration

### API Keys

Create a `.env` file in the project root and add your keys:

```
OPENROUTER_API_KEY=sk-or-v1-your-key-here
OPENAI_API_KEY=sk-proj-your-key-here
PINECONE_API_KEY=your-pinecone-key-here
```

Detailed instructions: `API_KEYS_SETUP.md`

### Ports

Default ports:

* Frontend: 3000
* Backend: 8000

---

## Support

If you encounter issues:

1. Make sure ports **3000** and **8000** are not in use
2. Verify all dependencies are installed
3. Restart the project using:

   ```bash
   ./start.sh
   ```

---

##  Future Enhancements

1. Real-time collaboration (WebSockets)
2. Multi-modal AI (audio + image + text)
3. Mobile app (React Native)
4. Advanced analytics dashboard

## If you want see more information please read QUIKSTART.md, ARCHITECTURE.md, API.md.!!!

BioSpaceSearch — explore space with the power of AI!

