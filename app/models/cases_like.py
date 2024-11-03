# encoding: utf-8
# @File  : cases_like.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/31
from sqlalchemy import Column, INT
from app.models.base import FunBaseModel


class DataFactoryCasesLike(FunBaseModel):
    """点赞表"""
    __tablename__ = 'data_factory_cases_like'

    cases_id = Column(INT, nullable=False, comment="造数场景id")

    def __init__(self, cases_id, user, del_flag=0, id=None):
        super().__init__(cases_id=user['id'], cases_name=user['username'], del_flag=del_flag, id=id)
        self.cases_id = cases_id
