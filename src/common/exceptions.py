from enum import Enum

class AppException(Exception):
   def __init__(self, code: str, message: str, status_code: int):

      self.code = code
      self.message = message
      self. status_code = status_code

class ErrorCode(str, Enum):
   """ Error codes for the application """

   USER_NOT_FOUND="USER_NOT_FOUND"