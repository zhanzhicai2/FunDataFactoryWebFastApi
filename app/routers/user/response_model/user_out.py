# encoding: utf-8
# @File  : user_out.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/16

from app.commons.responses.response_model import BaseDto
from datetime import datetime


class SearchUserDto(BaseDto):
    id: int
    username: str
    name: str
    email: str


class UserDto(SearchUserDto):
    role: int
    is_valid: bool
    create_time: datetime
    last_login_time: datetime


class UserTokenDto(UserDto):
    token: str
