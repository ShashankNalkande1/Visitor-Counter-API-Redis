from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .api.routes import router
from .services.like_service import LikeService
from .redis_client import RedisClient

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure Redis key exists (idempotent)
    LikeService.ensure_key_exists()
    yield
    # Shutdown: clean up Redis connection
    await RedisClient.close()

app = FastAPI(title="Instagram Heart API with Redis", lifespan=lifespan)

# Include API routes
app.include_router(router)

# Serve the HTML UI
HTML_FILE = Path(__file__).parent / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    return HTMLResponse(content=HTML_FILE.read_text(encoding="utf-8"))