from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class UserCreateRequest(BaseModel):
   username: str = Field(
      ..., # required
      min_length=2,
      max_length=50
   )
   email: EmailStr
   hashed_password: str

class UserUpdateRequest(BaseModel):
   username: Optional[str] = Field(
      # ..., # required
      default=None, # optional
      min_length=2,
      max_length=50
   )
   email: Optional[EmailStr] = Field(default=None) # optional
   hashed_password: Optional[str] = Field(
      default=None, # optional
      min_length=8, # password at least 8 chars
   )

   def has_at_least_one_field(self) -> bool:
      """ check if at least one field is provided """

      # any returns True -- if at least one item in the list is True -- False otherwise
      return any([
         self.username is not None,
         self.email is not None,
         self.hashed_password is not None,
      ])

class UserResponse(BaseModel):
   id: int
   username: str
   email: EmailStr
   created_at: datetime