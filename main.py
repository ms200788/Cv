from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os, re

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- HEALTH ----------
@app.get("/health")
async def health():
    return {"status": "alive"}

# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
async def home():
    index_path = os.path.join(BASE_DIR, "index.html")
    if not os.path.isfile(index_path):
        return HTMLResponse("index.html not found", status_code=500)
    return FileResponse(index_path, media_type="text/html")

# ---------- DYNAMIC PAGES ----------
@app.get("/{page}", response_class=HTMLResponse)
async def serve_page(page: str):
    # allow only safe slugs
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", page):
        return HTMLResponse("Not found", status_code=404)

    file_path = os.path.join(BASE_DIR, f"{page}.html")

    if not os.path.isfile(file_path):
        return HTMLResponse("Page not found", status_code=404)

    return FileResponse(file_path, media_type="text/html")