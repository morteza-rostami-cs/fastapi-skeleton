from fastapi import FastAPI
from pathlib import Path # for joining path
from fastapi.responses import FileResponse

from src.users.routes import register_user_routes
# error handler
from src.common.handlers import register_exception_handlers
from fastapi.staticfiles import StaticFiles

# get parent dir of main.py
BASE_DIR = Path(__file__).resolve().parent

# fastapi main app
app = FastAPI()

# serve static files
app.mount(
   "/static",
   StaticFiles(directory=BASE_DIR / "frontend"),
   name="static",
)

# register global error handler
register_exception_handlers(app=app)

# register users routes
register_user_routes(app=app)

# frontend routes
@app.get("/", include_in_schema=False)
def home():
   # serve html file
   return FileResponse(BASE_DIR / "frontend" / "index.html")

@app.get("/register", include_in_schema=False)
def register_page():
   return FileResponse(BASE_DIR / "frontend" / "register.html")