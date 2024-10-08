from datetime import datetime
from app.models import Session
from sqlalchemy import or_, func, asc
from app.models.user import DataFactoryUser
from app.commons.utils.logger import Log
# from app.routers.user.user_schema import LoginUserBody, UpdateUserBody, SearchUserBody
from app.routers.user.user_schema import LoginUserBody, UpdateUserBody, SearchUserBody
from config import Permission
from app.commons.utils.db_utils import DbUtils
from app.commons.exceptions.global_exception import BusinessException
from loguru import logger


class UserDao(object):
    log = Log('UserDao')

    @classmethod
    def register_user(cls, username: str, name: str, password: str, email: str) -> None:
        """
        :param username: 用户名
        :param name: 姓名
        :param password: 密码
        :param email: 邮箱号
        :return:
        """
        with Session() as session:
            # 先查询用户名或邮箱号是否重复
            users = session.query(DataFactoryUser).filter(
                or_(DataFactoryUser.username == username, DataFactoryUser.email == email)).first()
            if users:
                raise BusinessException('用户名或邮箱号重复')
            # 统计用户表的用户数
            count = session.query(func.count(DataFactoryUser.id)).group_by(DataFactoryUser.id).count()
            user = DataFactoryUser(username, name, password, email)
            # 如果第一个进来，默认是管理员权限
            if count == 0:
                user.role = Permission.ADMIN
            session.add(user)
            session.commit()

    @classmethod
    def user_login(cls, data: LoginUserBody) -> DataFactoryUser:
        """
        :param data: 用户模型
        :return:
        """
        with Session() as session:
            user = session.query(DataFactoryUser).filter(DataFactoryUser.username == data.username,
                                                         DataFactoryUser.password == data.password).first()
            if user is None:
                raise BusinessException("用户名或密码错误")
            if user.is_valid:
                # is_valid == true, 说明被冻结了
                raise BusinessException("对不起, 你的账号已被冻结, 请联系管理员处理")
            user.last_login_time = datetime.now()
            session.commit()
            # 进行对象刷新，更新对象，让对象过期，从而在下次访问时重新加载
            session.refresh(user)
            return user

    @classmethod
    def get_user_infos(cls, page: int = 1, limit: int = 10, search: str = None) -> (int, DataFactoryUser):
        """
                :param page: 页码
                :param limit: 多少条一页
                :param search: 搜索内容
                :return:
                """
        """获取用户信息列表"""
        with Session() as session:
            filter_list = []
            data = session.query(DataFactoryUser)
            if search:
                filter_list.append(DataFactoryUser.username.like(f"%{search}%"))
            user_infos = data.order_by(asc(DataFactoryUser.id)).filter(*filter_list)
            total = user_infos.count()
            return total, user_infos.limit(limit).offset((page - 1) * limit).all()

    @classmethod
    def search_user(cls, data: SearchUserBody) -> DataFactoryUser:
        """
        搜索用户
        :param cls:
        :param data:
        :return:
        """
        with Session() as session:
            filter_list = [DataFactoryUser.is_valid == False]
            # filter_list = [DataFactoryUser.is_valid == False]
            user_query = session.query(DataFactoryUser)
            filter_list.append(
                or_(DataFactoryUser.username.like(f"%{data.keyword}%"), DataFactoryUser.name.like(f"%{data.keyword}%"),
                    DataFactoryUser.email.like(f"%{data.keyword}%")))
            user = user_query.filter(*filter_list)
            return user.all()

    @classmethod
    def update_user(cls, data: UpdateUserBody, user_data: dict) -> None:
        """
        :param user_data: 用户数据
        :param data: 更新的数据
        :return:
        """
        with Session() as session:
            user = session.query(DataFactoryUser).filter(DataFactoryUser.username == data.username).first()
            if user is None:
                raise BusinessException("用户不存在")
            DbUtils.update_model(user, data.dict(), user_data, not_null=True)
            session.commit()
