import os


# 启动配置
class Config(object):
    """
    配置类
    #数据库连接信息
    """
    HOST = "127.0.0.1"
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "root"
    DBNAME = "fun"

    # 数据库配置
    SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    KEY = "funDataFactory"


class Text(object):
    """描述配置"""
    TITLE = "Fun数据工厂"
    VERSION = "v1.0"
    DESCRIPTION = "欢迎来到方总的数据工厂"


class FilePath(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 后端服务项目目录

    APP_PATH = os.path.join(BASE_DIR, "app")  # app 路径

    CURD_PATH = os.path.join(APP_PATH, "curd")  # dao路径

    LOG_FILE_PATH = os.path.join(BASE_DIR, "logs")  # 日志文件路径
    if not os.path.isdir(LOG_FILE_PATH): os.mkdir(LOG_FILE_PATH)

    LOG_NAME = os.path.join(LOG_FILE_PATH, 'FunDataFactory.log')


class Permission(object):
    MEMBERS = 0  # 普通用户
    LEADER = 1  # 组长
    ADMIN = 2  # 超管


HTTP_CODE_MSG = {

    404: '请求路径找不到',
    405: '请求方法不支持',
    408: '请求超时',
    500: '服务器内部错误',
    302: '请求方法不支持'
}
