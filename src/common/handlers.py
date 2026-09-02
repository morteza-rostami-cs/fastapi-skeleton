from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.common.exceptions import AppException


def register_exception_handlers(app: FastAPI):

   @app.exception_handler(AppException)
   async def handle_app_exception(
      request: Request,
      exc: AppException,
   ):
      return JSONResponse(
         status_code=exc.status_code,
         content={
            "code": exc.code,
            "message": exc.message,
         },
      )