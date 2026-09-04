from fastapi import FastAPI, Path, Query, Body, HTTPException, status
from fastapi.responses import JSONResponse

# url parameter /users/{id}
# query parameters /users?page=2&limit=10

# http validation
from src.users.schemas import (
   UserCreateRequest,
   UserUpdateRequest,
   UserResponse,
)

from src.common.exceptions import AppException, ErrorCode
from src.common.schemas import ErrorResponse # global response error schema

from src.common.constants import API_PREFIX
from src.users.repository import UserRepository

from src.users.model import User

def register_user_routes(app: FastAPI, repository: UserRepository):
   
   @app.get(
      f"{API_PREFIX}/users",
      response_model=list[UserResponse]
      )
   def get_users(
      page: int = Query(default=1), # page=1
      limit: int = Query(default=10) # get 10 at a time
   ):

      users = repository.get_all()

      # exclude hashed_password
      return [
         user.model_dump(exclude={"hashed_password"})
         for user in users
      ]      


   @app.get(
      f"{API_PREFIX}/users/{{user_id}}",
      response_model=UserResponse,
      responses={
         # 404 -- has this Error schema (openapi)
         404: {"model": ErrorResponse},
      }
   )
   def get_user(
      # url parameter
      user_id: int = Path(..., gt=0, description="The id of the user to get")
      ):

      user = repository.get_by_id(user_id=user_id)

      if not user:
         # fastapi turns this into an HTTP response
         raise AppException(
            code=ErrorCode.USER_NOT_FOUND.value,
            message=f"user with {user_id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
         )

      return user.model_dump(
         exclude={"hashed_password"}
      )

   @app.post(
      f"{API_PREFIX}/users",
      response_model=UserResponse,
      status_code=201, # new resource created
      )
   def create_user(
      user: UserCreateRequest = Body(...)
      ):

      # make a new user object using model
      new_user = User(
         username=user.username,
         email=user.email,
         hashed_password=user.hashed_password,
      )

      # create a user in db
      created_user = repository.create(new_user)

      return created_user.model_dump(
         exclude={"hashed_password"},
      )

   @app.put(
      f"{API_PREFIX}/users/{{user_id}}",
      response_model=UserResponse,
      )
   def update_user(
      data: UserUpdateRequest = Body(...), # body
      user_id: int = Path(..., gt=0)
   ):

      # check: if at least one field is provided
      if not data.has_at_least_one_field():
         raise AppException(
            code=ErrorCode.INVALID_INPUT,
            message=f"at least provide one field",
            status_code=status.HTTP_400_BAD_REQUEST,
         )

      # find the user
      user = repository.get_by_id(user_id)

      if not user:
         raise AppException(
            code=ErrorCode.USER_NOT_FOUND.value,
            message=f"user with {user_id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
         )

      # update user 

      # user.username = data.name
      # user.email = data.name

      # update only the provided fields
      update_data = data.model_dump(
         exclude_unset=True, # remove the empty values
         exclude_none=True,
      )

      # set new values on user
      for field, value in update_data.items():
         setattr(
            user, # obj
            field, # name
            value, # value
         )

      updated_user = repository.update(user)

      return updated_user.model_dump(
         exclude={"hashed_password"},
      )

   @app.delete(
      f"{API_PREFIX}/users/{{user_id}}", 
      response_model=UserResponse)
   def delete_user(
      # ... means required
      user_id: int = Path(..., gt=0)
   ):
      # find user 
      user = repository.get_by_id(user_id)

      if not user:
         raise AppException(
            code=ErrorCode.USER_NOT_FOUND.value,
            message=f"user with {user_id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
         )

      # delete from db
      deleted_user = repository.delete(user)

      return deleted_user.model_dump(
         exclude={"hashed_password"},
      )