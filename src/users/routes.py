from fastapi import FastAPI, Path, Query, Body
from fastapi.responses import JSONResponse

# url parameter /users/{id}
# query parameters /users?page=2&limit=10

def register_user_routes(app: FastAPI):

   users = [
      {"id": 1, "name": "Alice"},
      {"id": 2, "name": "Bob"},
      {"id": 3, "name": "Charlie"},
   ]
   
   @app.get("/users")
   def get_users(
      page: int = Query(default=1), # page=1
      limit: int = Query(default=10) # get 10 at a time
   ):

      # start index
      start = (page - 1) * limit
      # end index
      end = start + limit
      
      return users[start:end]


   @app.get("/users/{user_id}")
   def get_user(
      # url parameter
      user_id: int = Path(..., gt=0, description="The id of the user to get")
      ):
      for user in users:
         if user["id"] == user_id:
            return user

      return JSONResponse(
         status=404,
         content={
            "error": "user not found",
            "message": f"no user with {user_id} exists",
            "user_id": user_id
         }
      )

   @app.post("/users")
   def create_user(user: any = Body(...)):
      users.append(user)

      return user

   @app.put("/users/{user_id}")
   def update_user(
      user_id: int = Path(..., gt=0)
   ):
      for user in users:
         if user["id"] == user_id:
            user["name"] = "update name"
            return user

      return JSONResponse(
         status_code=404,
         content={
            "error": "user not found",
            "message": f"no user with {user_id} exists",
            "user_id": user_id,
         },
      )

   @app.delete("/users/{user_id}")
   def delete_user(
      # ... means required
      user_id: int = Path(..., gt=0)
   ):
      for index, user in enumerate(users):
         if user["id"] == user_id:
            deleted_user = users.pop(index)

            return deleted_user

      return JSONResponse(
         status_code=404,
         content={
            "error": "user not found",
            "message": f"no user with {user_id} exists",
            "user_id": user_id,
         },
      )