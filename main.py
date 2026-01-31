from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "html")

# ---------- HOME ----------
@app.get("/", response_class=HTMLResponse)
async def home():
    return FileResponse(os.path.join(HTML_DIR, "page1.html"))

# ---------- PAGE 2 ----------
@app.get("/page2", response_class=HTMLResponse)
async def page2():
    return FileResponse(os.path.join(HTML_DIR, "page2.html"))

# ---------- PAGE 3 ----------
@app.get("/page3", response_class=HTMLResponse)
async def page3():
    return FileResponse(os.path.join(HTML_DIR, "page3.html"))

# ---------- HEALTH ----------
@app.get("/health")
async def health():
    return {"status": "alive"}
