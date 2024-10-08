# encoding: utf-8
# @File  : context_utils.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/05

import contextvars

from starlette.requests import Request

# 当前请求对象上下
REQUEST_CONTEXT: contextvars.ContextVar[Request] = contextvars.ContextVar('request', default=None)
