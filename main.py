from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os, re

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")

# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse(
        os.path.join(HTML_DIR, "index.html"),
        media_type="text/html"
    )

# ---------- DYNAMIC PAGES ----------
@app.get("/{page}", response_class=HTMLResponse)
async def serve_page(page: str):
    # allow only safe slugs like articles, ai-guide, telegram_bot
    if not re.match(r"^[a-zA-Z0-9_-]+$", page):
        return HTMLResponse("Not found", status_code=404)

    path = os.path.join(HTML_DIR, f"{page}.html")

    if not os.path.isfile(path):
        return HTMLResponse("Page not found", status_code=404)

    return FileResponse(path, media_type="text/html")

# ---------- HEALTH ----------
@app.get("/health")
async def health():
    return {"status": "alive"}