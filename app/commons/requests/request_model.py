# encoding: utf-8
# @File  : request_model.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/10

from pydantic import BaseModel

from app.constants.constants import ERROR_MSG_TEMPLATES


class BaseBody(BaseModel):
    # 入参基础模型
    class Config:
        error_msg_templates = ERROR_MSG_TEMPLATES


class ToolsSchemas(object):
    @staticmethod
    def not_empty(v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise ValueError("不能为空")
        return v



