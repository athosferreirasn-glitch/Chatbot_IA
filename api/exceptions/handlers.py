from fastapi import Request
from app.exceptions.custom_exception import BusinessException
from fastapi.responses import JSONResponse
from main import app

@app.exception_handler(BusinessException)
def business_exception_handler(
    request: Request,
    exc: BusinessException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail
        }
    )