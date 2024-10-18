# encoding: utf-8
# @File  : test.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/16
from pydantic import BaseModel, Field, EmailStr, ValidationError


class RegisterUserBody(BaseModel):
    username: str = Field(..., title="用户名", description="必传")
    password: str = Field(..., title="密码", description="必传")
    name: str = Field(..., title="姓名", description="必传")
    email: EmailStr = Field(..., title="邮箱号", description="必传")

    class Config:
        error_msg_templates = {
            'value_error.missing': '不能为空'
        }


try:
    RegisterUserBody(username='x')
except ValidationError as e:
    print(e)
