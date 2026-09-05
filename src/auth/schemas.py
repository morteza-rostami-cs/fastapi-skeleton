from pydantic import BaseModel, Field, EmailStr
# from datetime import datetime
# from typing import Optional

class RegisterRequest(BaseModel):
   email: EmailStr = Field(...)
   password: str = Field(
      min_length=8, # password at least 8 chars
   )

