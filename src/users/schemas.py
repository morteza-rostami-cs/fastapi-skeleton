from pydantic import BaseModel, Field

class UserCreateRequest(BaseModel):
   name: str = Field(
      ..., # required
      min_length=2,
      max_length=50
   )

class UserUpdateRequest(BaseModel):
   name: str = Field(
      ..., # required
      min_length=2,
      max_length=50
   )

class UserResponse(BaseModel):
   id: int
   name: str