# -*- coding: utf-8 -*-
# @Time : 2022/6/12 22:06
# @Author : junjie
# @File : ProjectDao.py

from sqlalchemy import or_, desc

from app.curd.project_role.ProjectRoleDao import ProjectRoleDao
from app.models import Session
from app.models.project import DataFactoryProject
from app.models.user import DataFactoryUser
from app.routers.project.project_schema import AddProject, EditProject
from app.commons.utils.db_utils import DbUtils
from app.commons.utils.logger import Log
from app.commons.exceptions.global_exception import BusinessException
from config import Permission


class ProjectDao(object):
    log = Log("ProjectDao")

    @classmethod
    def insert_project(cls, form: AddProject, user: dict) -> None:
        with Session() as session:
            # session.expire_on_commit = False
            user_query = session.query(DataFactoryUser.username).filter(DataFactoryUser.username == form.owner).first()
            # user_query = session.query(DataFactoryUser.username).first()
            if user_query is None:
                raise BusinessException("用户不存在！！！")
            project = session.query(DataFactoryProject).filter(or_(DataFactoryProject.project_name == form.project_name,
                                                                   DataFactoryProject.git_project == form.git_project),
                                                               DataFactoryProject.del_flag == 0).first()
            if project:
                raise BusinessException("项目名或者git项目名重复, 请重新录入！！！")
            projects = DataFactoryProject(form, user)
            session.add(projects)
            session.commit()

    @classmethod
    def update_project(cls, data: EditProject, user: dict) -> None:
        """
        编辑项目
        :param data: 编辑项目模型
        :param user: 用户数据
        :return:
        """
        with Session() as session:
            ProjectRoleDao.operation_permission(data.id, user)
            project = session.query(DataFactoryProject).filter(DataFactoryProject.id == data.id,
                                                               DataFactoryProject.del_flag == 0).first()
            if project is None: raise BusinessException("项目不存在")
            # 根据名称查出数据
            project_name = session.query(DataFactoryProject).filter(
                DataFactoryProject.project_name == data.project_name,
                DataFactoryProject.del_flag == 0).first()
            # 如果有数据且主键id与请求参数id不相等
            if project_name is not None and project_name.id != data.id:
                raise BusinessException("项目名重复, 请重新录入！！！")
            git_project_name = session.query(DataFactoryProject).filter(
                DataFactoryProject.git_project == data.git_project,
                DataFactoryProject.del_flag == 0).first()
            if git_project_name is not None and git_project_name.id != data.id:
                raise BusinessException("git项目名重复, 请重新录入！！！")
            DbUtils.update_model(project, data.dict(), user)
            session.commit()

    @classmethod
    def delete_project(cls, id: int, user: dict) -> None:
        """删除项目"""
        with Session() as session:
            ProjectRoleDao.operation_permission(id, user)
            project = session.query(DataFactoryProject).filter(DataFactoryProject.id == id,
                                                               DataFactoryProject.del_flag == 0).first()
            if project is None:
                raise BusinessException("项目不存在")
            DbUtils.delete_model(project, user)
            session.commit()
            session.refresh(project)
            return project

    @classmethod
    def list_project(cls, user: dict, page: int = 1, size: int = 10, search: str = None) -> (int, DataFactoryProject):
        """
        获取项目列表
        :param user:
        :param page: 页码
        :param size: 大小
        :param search: 搜索内容
        :return:
        """
        with Session() as session:
            filter_list = [DataFactoryProject.del_flag == 0, *cls.user_all_projects(user)]
            if search:
                filter_list.append(DataFactoryProject.project_name.like(f"%{search}%"))
            project = session.query(DataFactoryProject).filter(*filter_list)
            project_infos = project.order_by(desc(DataFactoryProject.update_time)).limit(size).offset(
                (page - 1) * size).all()
            total = project.count()
        return total, project_infos

    # def list_project(cls, page: int = 1, size: int = 10, search: str = None) -> (int, DataFactoryProject):
    #     """
    #     获取项目列表
    #     # :param user:
    #     :param page: 页码
    #     :param size: 大小
    #     :param search: 搜索内容
    #     :return:
    #     """
    #
    #     with Session() as session:
    #         # filter_list = [DataFactoryProject.del_flag == 0, *cls.user_all_projects(user)]
    #         # filter_list = [*cls.user_all_projects(user)]
    #         filter_list = [DataFactoryProject.del_flag == 0]
    #         if search:
    #             filter_list.append(DataFactoryProject.project_name.like(f"%{search}%"))
    #         project = session.query(DataFactoryProject).filter(*filter_list)
    #         project_infos = project.order_by(desc(DataFactoryProject.update_time)).limit(size).offset(
    #             (page - 1) * size).all()
    #         total = project.count()
    #     return total, project_infos

    @classmethod
    def user_all_projects(cls, user):
        filter_list = []
        # 如果不是管理员角色
        if user['role'] != Permission.ADMIN:
            # 找出用户权限范围内的所有项目
            project_ids = ProjectRoleDao.project_by_user(user)
            # 公开的项目 或者 权限范围内的项目 或者 项目负责人的项目
            filter_list.append(or_(DataFactoryProject.id.in_(project_ids), DataFactoryProject.owner == user['username'],
                                   DataFactoryProject.private == False))
        return filter_list

    @classmethod
    def project_detail(cls, id: int, user: dict) -> DataFactoryProject:
        """获取项目详情"""
        with Session() as session:
            ProjectRoleDao.read_permission(id, user)
            project = session.query(DataFactoryProject).filter(DataFactoryProject.id == id,
                                                               DataFactoryProject.del_flag == 0).first()
            if project is None:
                raise BusinessException("项目不存在")
            return project
