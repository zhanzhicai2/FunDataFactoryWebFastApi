from datetime import datetime

from pydantic import BaseModel
from typing import Any

from sqlalchemy import Column, INT, DATETIME, SMALLINT, String, func

from app.models import Base


class ResponseDto(BaseModel):
    code: int = 200
    msg: str = '请求成功'
    data: Any = None


class ToolsSchemas(object):

    @staticmethod
    def not_empty(v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise ValueError("不能为空")
        return v


class ListDto(BaseModel):
    total: int = 0
    lists: list = []


class FunBaseModel(Base):
    id = Column(INT, primary_key=True, comment="主键id")
    create_time = Column(DATETIME, nullable=False, comment="创建时间")
    update_time = Column(DATETIME, onupdate=func.now(), nullable=False, comment="更新时间")
    del_flag = Column(SMALLINT, default=0, nullable=False, comment="0: 未删除 1: 已删除")
    create_code = Column(String(20), nullable=True, comment="创建人编码")
    create_name = Column(String(20), nullable=True, comment="创建人")
    update_code = Column(String(20), nullable=True, comment="更新人编码")
    update_name = Column(String(20), nullable=True, comment="更新人")
    # 设置为True，代表为基类，不会被创建为表
    __abstract__ = True

    def __init__(self, create_code=None, create_name=None, update_code=None, update_name=None, del_flag=0, id=None):
        self.id = id
        self.create_time = datetime.now()
        self.update_time = datetime.now()
        self.del_flag = del_flag
        self.create_code = create_code
        self.create_name = create_name
        self.update_code = update_code
        self.update_name = update_name
