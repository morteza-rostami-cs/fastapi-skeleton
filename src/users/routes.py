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

def register_user_routes(app: FastAPI):

   users = [
      {"id": 1, "name": "Alice"},
      {"id": 2, "name": "Bob"},
      {"id": 3, "name": "Charlie"},
   ]
   
   @app.get(
      "/users",
      response_model=list[UserResponse]
      )
   def get_users(
      page: int = Query(default=1), # page=1
      limit: int = Query(default=10) # get 10 at a time
   ):

      # start index
      start = (page - 1) * limit
      # end index
      end = start + limit
      
      return users[start:end]


   @app.get(
      "/users/{user_id}",
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
      for user in users:
         if user["id"] == user_id:
            return user

      # fastapi turns this into an HTTP response
      raise AppException(
         code=ErrorCode.USER_NOT_FOUND.value,
         message=f"user with {user_id} does not exist",
         status_code=status.HTTP_404_NOT_FOUND,
      )

   @app.post(
      "/users",
      response_model=UserResponse,
      status_code=201, # new resource created
      )
   def create_user(
      user: UserCreateRequest = Body(...)
      ):

      # create a new user
      new_user = {
         "id": len(users) + 1,
         "name": user.name
      }

      users.append(new_user)

      return new_user

   @app.put(
      "/users/{user_id}",
      response_model=UserResponse,
      )
   def update_user(
      data: UserUpdateRequest = Body(...), # body
      user_id: int = Path(..., gt=0)
   ):
      for user in users:
         if user["id"] == user_id:
            user["name"] = data.name
            return user

      raise AppException(
         code=ErrorCode.USER_NOT_FOUND.value,
         message=f"user with {user_id} does not exist",
         status_code=status.HTTP_404_NOT_FOUND,
      )

   @app.delete("/users/{user_id}", response_model=UserResponse)
   def delete_user(
      # ... means required
      user_id: int = Path(..., gt=0)
   ):
      for index, user in enumerate(users):
         if user["id"] == user_id:
            deleted_user = users.pop(index)

            return deleted_user

      raise AppException(
         code=ErrorCode.USER_NOT_FOUND.value,
         message=f"user with {user_id} does not exist",
         status_code=status.HTTP_404_NOT_FOUND,
      )