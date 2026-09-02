from pydantic import BaseModel

# global Error shapes

# this is for documentation (openapi)
class ErrorResponse(BaseModel):
   code: str
   message: str