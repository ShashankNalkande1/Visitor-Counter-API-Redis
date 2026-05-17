````markdown
# 🚀 Visitor Counter API with Redis ❤️

<div align="center">

<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-Cache%20Engine-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black"/>

<br/>
<br/>

### ⚡ Real-Time Instagram Style Like Counter using FastAPI + Redis

💻 Built for learning:
**Redis Caching • FastAPI APIs • Real-Time State Management • Backend Architecture**

🔗 **Live Demo:**  
https://visitor-counter-api-redis-2.onrender.com/

🔗 **GitHub Repository:**  
https://github.com/ShashankNalkande1/fastapi_heart_redis

</div>

---

# 📌 Overview

This project simulates an **Instagram-style heart/like system** where users can:

- ❤️ Like a post
- 💔 Unlike a post
- ⚡ Instantly update like counts
- 🔥 Store data inside Redis
- 🖱 Double-tap to like

Instead of storing counts inside traditional databases, this project uses **Redis**, an ultra-fast in-memory data store built for real-time systems.

This is not just a UI project.

It demonstrates:
- Backend API engineering
- Redis integration
- State management
- Real-time interaction patterns
- Production deployment using Render

---

# 🧠 Why Redis?

Traditional databases are slower for ultra-frequent counters.

Redis stores data in memory, making operations insanely fast ⚡

Perfect for:
- Like counters
- Visitor counters
- Live analytics
- Sessions
- Notifications
- Rate limiting

This project demonstrates a real-world Redis use case used in large-scale systems.

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend API Framework |
| Redis | Real-Time Data Store |
| HTML/CSS/JS | Interactive Frontend |
| Render | Cloud Deployment |
| Python | Core Programming Language |

---

# ✨ Features

## ❤️ Real-Time Like Counter
Instantly increments/decrements likes using Redis.

## ⚡ Double Tap Interaction
Instagram-inspired UX interaction.

## 🔥 Redis Powered Backend
Ultra-fast in-memory operations.

## 🎨 Clean Interactive UI
Minimal Instagram-style frontend.

## 🌐 Production Deployment
Hosted live on Render.

---

# 📂 Project Structure

```bash
fastapi_heart_redis/
│
├── main.py                # FastAPI application
├── redis_client.py        # Redis connection logic
├── templates/             # HTML frontend
├── static/                # CSS / JS assets
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ShashankNalkande1/fastapi_heart_redis.git

cd fastapi_heart_redis
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn redis python-dotenv
```

---

# 🔥 Redis Configuration

## Local Redis Setup

Create a `.env` file:

```env
REDIS_URL=redis://localhost:6379
```

---

## Cloud Redis Example

```env
REDIS_URL=redis://default:password@host:6379
```

---

# ▶ Running the Application

```bash
uvicorn main:app --reload
```

Server starts on:

```bash
http://127.0.0.1:8000
```

---

# 🌍 Deployment

This project is deployed on Render 🚀

### Live URL:

https://visitor-counter-api-redis-2.onrender.com/

---

# 🧪 API Workflow

```text
User Clicks ❤️
       ↓
Frontend Sends Request
       ↓
FastAPI Receives API Call
       ↓
Redis Updates Counter
       ↓
Updated Count Returned
       ↓
UI Updates Instantly
```

---

# 📸 Core Redis Logic

```python
redis_client.incr("likes")
```

Increment like count instantly.

```python
redis_client.decr("likes")
```

Decrease like count.

This is the core concept behind:
- Instagram likes
- YouTube views
- Live visitor counters
- Reactions systems

---

# ⚠ Production Notes

This project is intentionally minimal and educational.

Production-grade systems would additionally include:
- Authentication
- User sessions
- Rate limiting
- Distributed Redis setup
- Error monitoring
- Persistent storage backup
- API security

---

# 🧠 What This Project Teaches

✅ FastAPI fundamentals  
✅ Redis integration  
✅ Real-time counters  
✅ API architecture  
✅ Frontend-backend communication  
✅ Environment variable management  
✅ Cloud deployment basics  

---

# 👨‍💻 Author

### Shashank Nalkande

Backend-focused engineer building scalable systems using:
- Python
- FastAPI
- Django
- Redis
- Backend Architecture

---

<div align="center">

## ⭐ If you found this useful, give the repository a star.

🔥 Build systems.  
⚡ Engineer performance.  
🧠 Master backend architecture.

</div>
````
