# encoding: utf-8
# @File  : git.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/10

from app.commons.settings.config import FilePath
from app.commons.utils.cmd_utils import CmdUtils
from urllib.parse import quote
from loguru import logger


class Git(object):

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
        logger.info("http开始克隆, 方式为http")
        command_str = f"cd {FilePath.BASE_DIR}\n" \
                      f"git clone -b {git_branch} {Git.git_url(git_url, user, password)}\n"
        CmdUtils.cmd(command_str)
        logger.info("http克隆结束")

    @staticmethod
    def git_clone_ssh(git_branch, git_url):
        """
        ssh克隆
        :param git_branch: 分支名
        :param git_url: 代码地址
        :return:
        """
        logger.info("ssh克隆开始")
        command_str = f"cd {FilePath.BASE_DIR}\n" \
                      f'git clone -b {git_branch} {git_url} --config core.sshCommand="ssh -i {FilePath.RSA_PRI_KEY}"\n'
        CmdUtils.cmd(command_str)
        logger.info("ssh克隆结束")

    @staticmethod
    def git_pull(project_path: str, git_branch: str) -> None:
        """
        拉起代码
        :param project_path:
        :param git_branch:
        :return:
        """
        logger.info("拉取项目代码开始")
        command_str = f"cd {project_path}\n" \
                      f"git fetch --all\n" \
                      f"git reset --hard origin/{git_branch}\n"
        CmdUtils.cmd(command_str)
        logger.info("拉取项目代码结束")


# if __name__ == '__main__':
#     # git_url = 'https://gitee.com/zhanzhicai/img'
#     git_url = 'git@gitee.com:zhanzhicai/img.git'
#     git_branch = 'master'
#     project = 'img'
#     user = 'zhanzhicai'
#     password = 'Zhanzhicai0502'
#     Git.git_clone_ssh(git_branch, git_url)
    # Git.git_clone_http(git_branch,git_url,user,password)
