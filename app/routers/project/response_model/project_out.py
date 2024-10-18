# encoding: utf-8
# @File  : project_out.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/10
from app.commons.responses.response_model import BaseDto
from datetime import datetime
from typing import Union


class ProjectDto(BaseDto):
    id: int
    project_name: str
    description: str = None
    directory: str
    owner: str
    private: bool
    pull_type: int
    git_project: str
    git_url: str
    git_branch: str
    git_account: str = None
    git_password: str = None
    create_time: datetime
    update_time: datetime
    del_flag: int
    create_id: int
    create_name: str
    update_id: int = None
    update_name: str = None


class ProjectDetailDto(ProjectDto):
    rsa_pub_key: Union[str, None]


class RoleDto(BaseDto):
    id: int
    username: str
    name: str
    email: str
    project_role: int
    project_id: int
    user_id: int
    create_name: str
    create_time: datetime
