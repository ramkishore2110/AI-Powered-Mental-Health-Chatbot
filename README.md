# 💬 SerenityBot – AI-Powered Mental Health Chatbot

**SerenityBot** is a compassionate, AI-driven mental health companion built for students and young adults. It offers real-time emotional support, intelligent therapeutic conversations, and a beautifully responsive interface powered by modern UI/UX design and advanced NLP models.

> 🧠 Built with GPT/Gemini, RoBERTa, FastAPI & React  
> 🎨 Glassmorphism UI with Light & Dark Modes  
> 🌿 Emotion-aware feedback and ambient soundscapes

---

## 🌟 Features

### 💡 Frontend (React + TypeScript)
- 🧊 **Glassmorphism Interface**: Clean, modern design with smooth animations
- 🌙 **Dual Theme Support**: Light and dark modes for comfort and accessibility
- 💭 **Real-time Emotion Sidebar**: Live emotion analysis as you type
- 🎵 **Therapeutic Soundscapes**: Ambient audio for calming experiences
- 📲 **Responsive Design**: Mobile-first and fully accessible

### ⚙️ Backend (FastAPI + Gemini/GPT + NLP)
- 🤖 **AI-Powered Replies**: GPT-4/Gemini 2.0-based therapeutic conversations
- 📈 **RoBERTa Emotion Detection**: Real-time mood recognition
- 🧠 **Crisis Detection**: Detects alarming statements or distress signals
- 🛡️ **Rate Limiting & Security**: Prevents misuse and ensures safe access
- 📊 **Health Monitoring**: System status and uptime checks

---

## 🚀 Quick Start

### ✅ Prerequisites
- Python 3.9+
- Node.js 16+
- Google Gemini API key or OpenAI key

---

### 1. 📦 Backend Setup

```bash
git clone https://github.com/yourusername/serenitybot.git
cd serenitybot/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Environment variables
cp .env.example .env
```

Edit `.env`:

```env
GOOGLE_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash-exp
PORT=8000
DEBUG=True
```

Start server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

### 2. 🌐 Frontend Setup

```bash
cd ../frontend
npm install
echo "REACT_APP_API_URL=http://localhost:8000/api/v1" > .env
npm start
```

Now visit `http://localhost:3000` to access the chatbot.

---

## 🧪 API Endpoints

| Endpoint                         | Description                        |
|----------------------------------|------------------------------------|
| `POST /api/v1/chat`              | Send message, get AI reply         |
| `POST /api/v1/emotions/analyze` | Analyze mood of a message          |
| `GET /api/v1/health`             | Basic system health check          |
| `WS /api/v1/chat/ws`             | WebSocket support (real-time chat) |

---

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

---

## 📁 Project Structure

```
serenitybot/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── utils/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   ├── .env
│   └── package.json
└── README.md
```

---

## 🔒 Security

- ✅ Input validation with Pydantic
- ✅ Rate limiting and abuse protection
- ✅ Crisis phrase detection
- ✅ CORS configured for safe frontend/backend communication

---

## 🙌 Team Members

> *Alphabetical Order*  
- Alvin Binu  
- Anagha Asok Kumar  
- Gowri Ajai  
- M S Mohemmad  
- Neha Nevin  
- Nikhil Krishnan M  
- Rehan Alex Rajeev  
- S R Ramkishore

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to modify, distribute, and share with attribution.
