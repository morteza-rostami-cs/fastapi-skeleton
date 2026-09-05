from fastapi import FastAPI, APIRouter, Body
from src.common.constants import API_PREFIX
from src.users.repository import UserRepository
"""
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/verification
GET  /api/auth/me
POST /api/auth/logout
"""
from src.auth.schemas import RegisterRequest
from src.users.model import User
import uuid
import bcrypt

def register_auth_routes(app: FastAPI, user_repo: UserRepository):

   router = APIRouter()

   @app.post(path="/register")
   def register(
      data: RegisterRequest = Body(...), 
   ):

      # hash password
      hashed_password = bcrypt.hashpw(
         data.password.encode("utf-8"),
         bcrypt.gensalt()
      )

      # create a new user
      new_user = User(
         username=str(uuid.uuid4()),
         email=data.email,
         hashed_password=hashed_password,
         email_verified=False, # not verified
      )


   app.include_router(router, prefix=f"{API_PREFIX}/auth")