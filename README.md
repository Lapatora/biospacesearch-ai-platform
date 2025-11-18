
# BioSpaceSearch AI Platform

AI platform for space research — a modern web application for analyzing space-related data using artificial intelligence.

---

## Features

* AI Chat — interact with the AI assistant
* File Management — upload and analyze documents
* User Profile — personalized settings
* Team Collaboration — work together on shared projects
* Data Analysis — AI automatically analyzes uploaded files

---



##  Application Preview



###  Registration
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 58 PM" src="https://github.com/user-attachments/assets/015c237f-ee25-4472-bbb4-e5f18ba23a51" />


###  AI Chat
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 43 PM" src="https://github.com/user-attachments/assets/010a93a8-b79f-4ab0-bba6-b1ec8c27b75f" />


###  Profile
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 46 PM" src="https://github.com/user-attachments/assets/08e44c65-72c4-4ba8-8caa-e5490fc6fa9a" />


###  Dashboard
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 34 PM" src="https://github.com/user-attachments/assets/ddd24739-ed59-4b1f-a398-858b2a4b142f" />


###  Theme Modes (Light / Dark)
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 46 PM" src="https://github.com/user-attachments/assets/42618b13-22f8-4e5a-825e-8cd7dc21d640" />
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 52 PM" src="https://github.com/user-attachments/assets/50e1f973-527b-458c-8e05-6221f8ae11a4" />


### � File Upload
<img width="1470" height="956" alt="Снимок экрана 2025-11-18 в 2 19 38 PM" src="https://github.com/user-attachments/assets/28d67670-9bf6-4909-8228-b1e84142c2a4" />






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

