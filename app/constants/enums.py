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
    members = 0  # 普通用户
    leader = 1  # 组长
    admin = 2  # 超管


class DeleteEnum(IntEnum):
    no = 0  # 未删除
    yes = 1  # 已删除


class ProjectRoleEnum(IntEnum):
    members = 0  # 普通用户
    leader = 1  # 组长


class PullTypeEnum(IntEnum):
    http = 0
    ssh = 1
