# encoding: utf-8
# @File  : global_exception.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/05

from app.commons.responses.response_code import CodeEnum
from typing import Any


class BusinessException(Exception):
    """业务异常处理类"""

    def __init__(self, msg: str = CodeEnum.BUSINESS_ERROR.msg) -> None:
        """
        初始化类
        :param msg:错误信息
        """
        self.code = CodeEnum.BUSINESS_ERROR.code
        self.msg = msg
        self.data = data


class AuthException(BusinessException):
    """登录态异常类"""

    def __init__(self, msg: str = CodeEnum.AUTH_ERROR.msg) -> None:
        self.code = CodeEnum.AUTH_ERROR.code
        self.msg = msg


class PermissionException(BusinessException):
    """用户权限不足异常类"""

    def __init__(self) -> None:
        self.code = CodeEnum.ROLE_ERROR.code
        self.msg = CodeEnum.ROLE_ERROR.msg
