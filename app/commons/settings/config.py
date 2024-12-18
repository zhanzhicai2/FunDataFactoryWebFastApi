import os
from app.constants import constants


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
    # KEY = "funDataFactory"
    # EXPIRED_HOUR = 12  # token过期时长
    #
    # AES_KEY = 'SVuRc6B7xsZnUWQO'  # AES 秘钥
    # AES_IV = 'MUnDCU0aADgs4hd1'  # AES 偏移量


class Text(object):
    """描述配置"""
    TITLE = "Fun数据工厂"
    VERSION = "v1.0"
    DESCRIPTION = "欢迎来到方总的数据工厂"


class FilePath(object):
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 后端服务项目目录

    SETS_PATH = os.path.dirname(os.path.abspath(__file__))  # settings目录
    COM_path = os.path.dirname(os.path.abspath(SETS_PATH))  # commons目录
    APP_PATH = os.path.dirname(os.path.abspath(COM_path))  # app 路径
    BASE_DIR = os.path.dirname(os.path.abspath(APP_PATH))  # 后端服务项目目录

    LOG_FILE_PATH = os.path.join(BASE_DIR, "../../../logs")  # 日志文件路径
    if not os.path.isdir(LOG_FILE_PATH): os.mkdir(LOG_FILE_PATH)
    FUN_SERVER = os.path.join(LOG_FILE_PATH, 'fun_server.log')

    FUN_ERROR = os.path.join(LOG_FILE_PATH, 'fun_error.log')

    CURD_PATH = os.path.join(APP_PATH, "crud")  # dao路径

    RSA_PUB_KEY = os.path.join(SETS_PATH, 'keys/rsa_pub_key')

    RSA_PRI_KEY = os.path.join(SETS_PATH, 'keys/rsa_pri_key')


# class Permission(object):
#
#     RSA_PRI_KEY = os.path.join(SETS_PATH, 'keys/rsa_pri_key')


HTTP_MSG_MAP = {

    404: '请求路径找不到',
    405: '请求方法不支持',
    408: '请求超时',
    500: '服务器内部错误',
    302: '请求方法不支持'
}
API_WHITE_LIST = [
    '/docs',
    '/static',
    '/favicon.ico',
    '/openapi.json',
    '/redoc',
    '/api/user/register',
    '/api/user/login',
    '/api/cases/out',
    '/api/cases/rpc/',
    '/api/project/gitSync'
]
API_ADMIN_LIST = [
    '/api/user/update'
]
API_LEADER_LIST = [
    '/api/project/insert'
]
# 项目日志滚动配置（日志文件超过10 MB就自动新建文件扩充）
LOGGING_ROTATION = "10 MB"
# 项目日志配置
LOGGING_CONF = {
    'server_handler': {
        'file': FilePath.FUN_SERVER,
        'level': 'INFO',
        'rotation': LOGGING_ROTATION,
        'enqueue': True,
        'backtrace': False,
        'diagnose': False,
    },
    'error_handler': {
        'file': FilePath.FUN_ERROR,
        'level': 'ERROR',
        'rotation': LOGGING_ROTATION,
        'enqueue': True,
        'backtrace': True,
        'diagnose': True,
    },
}
