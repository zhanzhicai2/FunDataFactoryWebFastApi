# encoding: utf-8
# @File  : get_project_path.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/22

from app.commons.settings.config import FilePath
import os


class ProjectPath(object):
    @staticmethod
    def get(project_name: str, directory_name: str) -> (str, str):
        """
        获取项目路径和脚本路径
        :param project_name:
        :param directory_name:
        :return: 项目目录，脚本目录
        """
        project_path = os.path.join(FilePath.BASE_DIR, project_name)
        if not os.path.isdir(project_path):
            raise Exception(f"找不到{project_name}这个项目")
        script_path = os.path.join(project_path, directory_name)
        if not os.path.isdir(script_path):
            raise Exception(f"找不到{directory_name}这个脚本目录")
        return project_path, script_path
