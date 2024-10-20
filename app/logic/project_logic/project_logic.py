# encoding: utf-8
# @File  : project_logic.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/13

import os
from app.crud.project.ProjectDao import ProjectDao
from app.crud.project_role.ProjectRoleDao import ProjectRoleDao
from app.routers.project.request_model.project_in import AddProject, EditProject, AddProjectRole, EditProjectRole
from app.commons.settings.config import FilePath
from app.core.git import Git
from app.commons.utils.aes_utils import AesUtils
from app.commons.utils.context_utils import REQUEST_CONTEXT
from app.constants.enums import PullTypeEnum
from app.commons.exceptions.global_exception import BusinessException


def insert_project_logic(body: AddProject):
    user = REQUEST_CONTEXT.get().user
    ProjectDao.insert_project(body, user)


def update_project_logic(body: EditProject):
    user = REQUEST_CONTEXT.get().user
    ProjectDao.update_project(body, user)


def delete_project_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    # todo: 暂时用不到，用_占坑，后续加入后置操作
    _ = ProjectDao.delete_project(id, user)


def get_project_lists_logic(page: int = 1, limit: int = 10, search=None):
    user = REQUEST_CONTEXT.get().user
    total, project_infos = ProjectDao.list_project(user, page, limit, search)
    project_lists = dict(total=total, lists=project_infos)
    return project_lists


def insert_project_role_logic(data: AddProjectRole):
    user = REQUEST_CONTEXT.get().user
    ProjectRoleDao.insert_project_role(data, user)


def update_project_role_logic(data: EditProjectRole):
    user = REQUEST_CONTEXT.get().user
    ProjectRoleDao.update_project_role(data, user)


def delete_project_role_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    ProjectRoleDao.delete_project_role(id, user)


def project_role_list_logic(project_id: int, page: int = 1, limit: int = 10, search=None):
    user = REQUEST_CONTEXT.get().user
    roles, count = ProjectRoleDao.project_role_list(user, project_id, page, limit, search)
    project_role_list = dict(total=count, lists=roles)
    return project_role_list


def read_project_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    ProjectRoleDao.read_permission(id, user)


def operation_project_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    ProjectRoleDao.operation_permission(id, user)


def init_project(id: int):
    user = REQUEST_CONTEXT.get().user
    project = ProjectDao.project_detail(id, user)
    project_path = os.path.join(FilePath.BASE_DIR, project.git_project)
    if os.path.isdir(project_path):
        raise BusinessException("项目已存在, 请执行刷新项目！")
    # 拉取项目
    if project.pull_type == PullTypeEnum.http.value:
        Git.git_clone_http(project.git_branch, project.git_url, project.git_account,
                           AesUtils.decrypt(project.git_password))
    else:
        Git.git_clone_ssh(project.git_branch, project.git_url)


def project_detail_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    rsa_pub_key = None
    project = ProjectDao.project_detail(id, user)
    if project.pull_type == PullTypeEnum.ssh.value:
        from app.commons.settings.config import FilePath
        with open(FilePath.RSA_PUB_KEY, 'r', encoding='utf-8') as f:
            rsa_pub_key = f.read()
    setattr(project, 'rsa_pub_key', rsa_pub_key)
    return project
