# Visitor Counter API with Redis

✨ A FastAPI-based project that tracks and displays likes for an Instagram-style post. The project uses Redis as a backend to store and manage the like counts efficiently.

## Features
- **Like Counter**: Users can like/unlike a post, and the like count updates in real-time.
- **Double-Tap to Like**: Simulates Instagram's double-tap like feature.
- **Redis Integration**: Uses Redis for fast and scalable data storage.
- **Interactive UI**: A visually appealing front-end built with HTML, CSS, and JavaScript.

---

## Prerequisites
- Python 3.8+
- Redis server installed and running
- A modern web browser for the front-end

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ShashankNalkande1/fastapi_heart_redis.git
   cd fastapi_heart_redis
```

2. **Install Dependencies**:
   ```bash
   pip install fastapi redis
   ```

3. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

---

## Usage
- Like a post by clicking the "Like" button.
- Unlike a post by clicking the "Unlike" button.
- The like count updates in real-time.

---

## Project Structure
- `main.py`: The FastAPI application.
- `redis_client.py`: A helper module for Redis operations.
- `templates/`: HTML templates for the front-end.

---

## Notes
- This project is a simple demonstration of FastAPI and Redis integration.
- For production use, additional features and error handling should be implemented.

## Configuration
- **REDIS_HOST**: The host address of the Redis server.
- **REDIS_PORT**: The port number of the Redis server.

---

## Running the Application
- Set the environment variables:
  ```bash
  REDIS_HOST=localhost
  REDIS_PORT=6379
  ```

- Run the application:
  ```bash
  uvicorn main:app --reload
  ```

