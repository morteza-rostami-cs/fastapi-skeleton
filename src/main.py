from fastapi import FastAPI

from src.users.routes import register_user_routes
# error handler
from src.common.handlers import register_exception_handlers

# fastapi main app
app = FastAPI()

@app.get("/")
def home():
   return dict(message="hi, fastapi")

# register global error handler
register_exception_handlers(app=app)

# register users routes
register_user_routes(app=app)