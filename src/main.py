from fastapi import FastAPI
from pathlib import Path # for joining path
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

from src.users.routes import register_user_routes
# error handler
from src.common.handlers import register_exception_handlers
from fastapi.staticfiles import StaticFiles

from src.database.connection import engine
from src.admin import register_admin

# repositories
from src.users.repository import UserRepository

# get parent dir of main.py
BASE_DIR = Path(__file__).resolve().parent

# runs on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
   print("app starts...")

   # connect to postgres
   with engine.connect() as connection:
      print("postgres connected successful") 

   # after this -- shutdown code
   yield

   print('app shutdown...') 

   # close db explicitly
   engine.dispose()

# fastapi main app
app = FastAPI(lifespan=lifespan)

# register admin
register_admin(app)

# serve static files
app.mount(
   "/static",
   StaticFiles(directory=BASE_DIR / "frontend"),
   name="static",
)

# register global error handler
register_exception_handlers(app=app)

# create repository
user_repo = UserRepository()

# register users routes
register_user_routes(app=app, repository=user_repo)

@app.get("/health/database")
def database_health():
   try:
      # open db connection 
      with engine.connect():
         return dict(
            status="ok",
            database="postgres",
         )
   except Exception:
      return dict(
         status="not ok",
         database="postgres",
      )


# frontend routes
@app.get("/", include_in_schema=False)
def home():
   # serve html file
   return FileResponse(BASE_DIR / "frontend" / "index.html")

# @app.get("/register", include_in_schema=False)
# def register_page():
#    return FileResponse(BASE_DIR / "frontend" / "register.html")