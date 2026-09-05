from fastapi import FastAPI
from pathlib import Path # for joining path
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

# error handler
from src.common.handlers import register_exception_handlers
from fastapi.staticfiles import StaticFiles

from src.database.connection import engine
from src.admin import register_admin

# repositories
from src.users.repository import UserRepository

# routes
from src.users.routes import register_user_routes
from src.jobs.routes import register_job_routes
from src.auth.routes import register_auth_routes

# redis connection
from src.redis.connection import redis_client

# background job stuff
from arq import create_pool
from arq.connections import RedisSettings
from src.common.settings import settings 

# arq redis pool
#arq_pool = None

# get parent dir of main.py
BASE_DIR = Path(__file__).resolve().parent

# runs on startup
# runs after router registration
@asynccontextmanager
async def lifespan(app: FastAPI):
   print("app starts...")

   # connect to postgres
   with engine.connect() as connection:
      print("postgres connected successful") 

   # connect redis
   await redis_client.ping()
   print("redis connected successfully")

   # connect arq and redis
   #global arq_pool

   app.state.arq_pool = await create_pool(
      # give arq a redis
      RedisSettings.from_dsn(
         str(settings.redis_url)
      )
   )
   print("arq connected success")

   # after this -- shutdown code
   yield

   print('app shutdown...') 

   # close arq pool
   await app.state.arq_pool.close()

   # close redis
   await redis_client.aclose()

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

# register jobs routes
register_job_routes(app=app)

# register users routes
register_user_routes(app=app, repository=user_repo)

register_auth_routes(app, user_repo=user_repo)

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

# redis health route
@app.get("/health/redis")
async def redis_health():
   try:
      await redis_client.ping()

      return dict(status="ok", redis="connected")
   except Exception:
      return dict(
         status="not ok",
         redis="not connected",
      )

# frontend routes
@app.get("/", include_in_schema=False)
def home():
   # serve html file
   return FileResponse(BASE_DIR / "frontend" / "index.html")

# @app.get("/register", include_in_schema=False)
# def register_page():
#    return FileResponse(BASE_DIR / "frontend" / "register.html")