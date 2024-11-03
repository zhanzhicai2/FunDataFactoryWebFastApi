# encoding: utf-8
# @File  : cases_out.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/01

from app.commons.responses.response_model import BaseDto
from datetime import datetime


class CaseGroupDto(BaseDto):
    group_name: str = None


class CaseDto(CaseGroupDto):
    id: int
    title: str = None
    name: str = None
    description: str = None
    header: str = None
    owner: str = None
    path: str = None
    param_in: str = None
    param_out: str = None
    example_param_in: str = None
    example_param_out: str = None


class CaseSearchDto(BaseDto):
    id: int
    title: str
    group_name: str


class CaseListDto(BaseDto):
    id: int
    title: str
    group_name: str
    description: str
    owner: str
    project_id: int
    like: bool
    like_num: int
    collection: bool
    collection_num: int
    update_time: datetime