from fastapi import FastAPI

from src.users.routes import register_user_routes

# fastapi main app
app = FastAPI()

@app.get("/")
def home():
   return dict(message="hi, fastapi")

# register users routes
register_user_routes(app=app)