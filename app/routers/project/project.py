# encoding: utf-8
# @File  : project.py
# @Author: 龟仙岛
# @Desc : 
# @Date  :  2024/09/09
from fastapi import APIRouter, Depends

from app import ResponseDto
from app.curd.project.ProjectDao import ProjectDao
from app.routers.project.project_schema import AddProject, ProjectResDto, EditProject, ProjectListResDto
from app.utils.auth_utils import Auth
from app.utils.exception_utils import NormalException
from config import Permission

router = APIRouter()


@router.post("/insert", name="新增项目", response_model=ProjectResDto)
def insert_project(body: AddProject, user=Depends(Auth(Permission.ADMIN))):
    try:
        project = ProjectDao.insert_project(body, user)
        return ProjectResDto(data=project, msg="新增成功")
    except Exception as e:
        raise NormalException(str(e))


@router.post("/update", name="编辑项目")
def update_project(body: EditProject, user=Depends(Auth(Permission.LEADER))):
    try:
        ProjectDao.update_project(body, user)
        return ResponseDto(msg="编辑成功")
    except Exception as e:
        raise NormalException(str(e))


@router.get("/delete", name="删除项目")
def delete_project(id: int, user=Depends(Auth(Permission.LEADER))):
    try:
        # 暂时用不到，用_占坑，后续加入后置操作
        # _ = ProjectDao.delete_project(id, user)
        return ResponseDto(msg="删除成功")
    except Exception as e:
        raise NormalException(str(e))


@router.get("/list", name="项目列表")
def get_project_infos(page: int = 1, limit: int = 10, search=None, _=Depends(Auth())):
    try:
        total, project_infos = ProjectDao.list_project(page, limit, search)
        return ProjectListResDto(data=dict(total=total, lists=project_infos))
    except Exception as e:
        raise NormalException(str(e))
