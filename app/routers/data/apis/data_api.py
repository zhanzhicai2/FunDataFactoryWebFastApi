# encoding: utf-8
# @File  : data_api.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/11

from app.logic.data_logic import data_logic
from app.commons.responses.response_model import ResponseDto


# 数据汇总
def data_summary():
    data = data_logic.data_summary_logic()
    return ResponseDto(data=data)
