import functools

from fastapi import HTTPException
from typing import Any


# 通用异常类
class NormalException(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=200, detail=detail)


def record_log(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        cls = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            func_name = func.__name__
            import traceback
            err = traceback.format_exc()
            cls.log.error(f"{func_name}失败:{err}")
            raise Exception(str(e))

    return wrapper
