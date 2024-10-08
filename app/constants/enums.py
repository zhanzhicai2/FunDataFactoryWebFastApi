# encoding: utf-8
# @File  : enums.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/04

from enum import Enum


class BaseEnum(Enum):
    """枚举基类"""

    @classmethod
    def get_member_values(cls):
        return [item.value for item in cls._member_map_.values()]

    @classmethod
    def get_member_names(cls):
        return [name for name in cls._member_names_]


class IntEnum(int, BaseEnum):
    """整数枚举"""
    pass


class PermissionEnum(IntEnum):
    MEMBERS = 0  # 普通用户
    LEADER = 1  # 组长
    ADMIN = 2  # 超管
