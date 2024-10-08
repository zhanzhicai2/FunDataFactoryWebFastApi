# encoding: utf-8
# @File  : expention_handler.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/04

from fastapi import Request

from config import HTTP_MSG_MAP
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from app.models.base import ResponseDto
from fastapi.responses import JSONResponse
from app.commons.exceptions.global_exception import BusinessException, AuthException, PermissionException
from pydantic import ValidationError
from app.commons.response.response_code import CodeEnum

from loguru import logger


# 自定义http异常处理器
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    res = ResponseDto(code=CodeEnum.HTTP_ERROR.code, msg=HTTP_MSG_MAP.get(exc.status_code, exc.detail))
    return JSONResponse(content=res.dict())


# 自定义参数校验异常处理器
async def validation_exception_handler(request: Request, err: RequestValidationError):
    message = ""
    data = {}
    for raw_error in err.raw_errors:
        if isinstance(raw_error.exc, ValidationError):
            exc = raw_error.exc
            if hasattr(exc, 'model'):
                fields = exc.model.__dict__.get('__fields')
                for field_key in fields.keys():
                    data[field_key] = fields.get(field_key).field_info.title
    for error in err.errors():
        field = str(error.get('loc')[-1])
        message += data.get(field, field) + ":" + str(error.get("msg")) + ","
    res = ResponseDto(code=CodeEnum.PARAMS_ERROR.code, msg=f"请求参数非法! {message[:-1]}")
    return JSONResponse(content=res.dict())


# 业务异常处理器
async def business_exception_handler(request: Request, exc: BusinessException):
    res = ResponseDto(code=exc.code, msg=exc.msg)
    return JSONResponse(content=res.dict())


# 权限异常处理器
async def role_exception_handler(request: Request, exc: PermissionException):
    res = ResponseDto(code=exc.code, msg=exc.msg)
    return JSONResponse(content=res.dict)


# 用户登录态异常处理处理器
async def auth_exception_handler(request: Request, exc: AuthException):
    res = ResponseDto(code=exc.code, msg=exc.msg)
    return JSONResponse(content=res.dict)


# 全局系统异常处理器(除了上面的异常，都归类到这里来，统一处理)
async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, PermissionException):
        return await role_exception_handler(request, exc)
    elif isinstance(exc, AuthException):
        return await auth_exception_handler(request, exc)
    elif isinstance(exc, BusinessException):
        return await business_exception_handler(request, exc)
    else:
        import traceback
        logger.exception(traceback.format_exc())
        res = ResponseDto(code=CodeEnum.SYSTEM_ERROR.code, msg=CodeEnum.SYSTEM_ERROR.msg)
        return JSONResponse(content=res.dict())