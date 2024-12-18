# encoding: utf-8
# @File  : project_api.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/16
from app.routers.project.request_model.project_in import AddProject, EditProject, AddProjectRole, EditProjectRole, GitProject
from app.commons.responses.response_model import ResponseDto, ListResponseDto
from app.logic.project_logic import project_logic


def insert_project(body: AddProject):
    project_logic.insert_project_logic(body)
    return ResponseDto(msg="新增成功")


def update_project(body: EditProject):
    project_logic.update_project_logic(body)
    return ResponseDto(msg="编辑成功")


def delete_project(id: int):
    project_logic.delete_project_logic(id)
    return ResponseDto(msg="删除成功")


def get_project_infos(page: int = 1, limit: int = 10, search=None):
    project_lists = project_logic.get_project_lists_logic(page, limit, search)
    return ListResponseDto(data=project_lists)


def insert_project_role(body: AddProjectRole):
    project_logic.insert_project_role_logic(body)
    return ResponseDto(msg="新增成功")


def update_project_role(body: EditProjectRole):
    project_logic.update_project_role_logic(body)
    return ResponseDto(msg="更新成功")


def delete_project_role(id: int):
    project_logic.delete_project_role_logic(id)
    return ResponseDto(msg="删除成功")


def project_role_list(project_id=None, page: int = 1, limit: int = 10, search=None):
    project_role_list = project_logic.project_role_list_logic(project_id, page, limit, search)
    return ListResponseDto(data=project_role_list)


def read_project(id: int):
    project_logic.read_project_logic(id)
    return ResponseDto()


def operation_project(id: int):
    project_logic.operation_project_logic(id)
    return ResponseDto()


def init_project(id: int):
    project_logic.init_project_logic(id)
    return ResponseDto(msg="初始化成功")


def project_detail(id: None):
    project = project_logic.project_detail_logic(id)
    return ResponseDto(data=project)


def sync_project(id: int):
    msg = project_logic.sync_project_logic_by_platform(id)
    return ResponseDto(msg=msg)


def sync_project_list():
    project = project_logic.sync_project_list_logic()
    return ResponseDto(data=project)


# git同步项目
def sync_project_by_git(body: GitProject):

    msg = project_logic.sync_project_logic_by_git(body)
    return ResponseDto(msg=msg)
