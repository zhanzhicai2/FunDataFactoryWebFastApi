# encoding: utf-8
# @File  : auth_utils.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/06
import jwt
from fastapi import Header
from jwt.exceptions import ExpiredSignatureError
from datetime import timedelta, datetime

from app.utils.exception_utils import AuthException, PermissionException
from config import Config, Permission


class UserToken(object):

    @staticmethod
    def get_token(data: dict) -> str:
        """
        :param data: 用户数据
        :return:
        """
        # 默认加密方式为 HS256, 过期时间 = 现在时间 + 配置过期时长
        token_data = dict({"exp": datetime.utcnow() + timedelta(hours=Config.EXPIRED_HOUR)}, **data)
        return jwt.encode(token_data, key=Config.KEY)

    @staticmethod
    def parse_token(token: str) -> dict:
        """解析token"""
        try:
            return jwt.decode(token, key=Config.KEY, algorithms=["HS256"])
        # token 过期
        except ExpiredSignatureError:
            raise Exception("token已过期, 请重新登录")
        # 解析失败
        except Exception:
            raise Exception("token解析失败, 请重新登录")


class Auth(object):

    def __init__(self, role: int = Permission.MEMBERS):
        self.role = role

    def __call__(self, token: str = Header(..., description="登录的token")):
        if not token:
            raise AuthException("token不能为空")
        try:
            user_info = UserToken.parse_token(token)
        except Exception as e:
            raise AuthException(str(e))
        if user_info.get('role', 0) < self.role:
            raise PermissionException('权限不足, 请联系管理员')
        return user_info
