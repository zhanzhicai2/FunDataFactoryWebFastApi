# encoding: utf-8
# @File  : git.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/10

from config import FilePath
from app.utils.logger import Log
from app.utils.cmd_utils import CmdUtils
from urllib.parse import quote


class Git(object):
    log = Log("git")

    @staticmethod
    def git_url(url, user, pwd):
        git_url_list = url.split('/')
        git_url_list[2] = f"{quote(user)}:{pwd}@" + git_url_list[2]
        return '/'.join(git_url_list)

    @staticmethod
    def git_clone_http(git_branch, git_url, user, password):
        """
        http克隆
        :param git_branch: 分支名
        :param git_url: 代码地址
        :param user: git账号
        :param password: git密码
        :return:
        """
        Git.log.info("开始克隆, 方式为http")
        command_str = f"cd {FilePath.BASE_DIR}\n" \
                      f"git clone -b {git_branch} {Git.git_url(git_url, user, password)}\n"
        CmdUtils.cmd(command_str)
        Git.log.info("克隆结束")
