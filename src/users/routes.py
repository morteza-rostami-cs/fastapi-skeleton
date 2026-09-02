from fastapi import FastAPI, Path
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
   def gets():
      return users


   @app.get("/users/{user_id}")
   def get_user(
      # url parameters
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