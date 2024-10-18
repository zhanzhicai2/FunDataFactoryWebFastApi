# encoding: utf-8
# @File  : auth_utils.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/09/06
from app.commons.settings import config
from app.commons.utils.jwt_utils import UserToken
from app.commons.utils.context_utils import REQUEST_CONTEXT
from app.commons.exceptions.global_exception import AuthException, PermissionException
from starlette.requests import Request
from app.constants.enums import PermissionEnum
from app.crud.user.UserDao import UserDao
from app.routers.user.response_model.user_out import UserDto


async def authentication(request: Request):
    # 从请求中获取token`
    token = request.headers.get('token') or None
    if not token:
        raise AuthException
    try:
        user_info = UserToken.parse_token(token)
    except Exception as e:
        raise AuthException(str(e))
    # # todo 通过user_id 查询用户信息
    # role = user_info.get('role') or PermissionEnum.MEMBERS.value
    # if role < PermissionEnum.ADMIN.value and str(request.url.path) in config.API_ADMIN_LIST:
    user = UserDao.get_with_id(id=user_info.get('id'))
    if user is None:
        raise AuthException("用户不存在")
    role = user.role or PermissionEnum.members.value
    if role < PermissionEnum.admin.value and str(request.url.path) in config.API_ADMIN_LIST:
        raise PermissionException()
    if role < PermissionEnum.leader.value and str(request.url.path) in config.API_LEADER_LIST:
        raise PermissionException()

    user_dict = UserDto.from_orm(user)
    request.scope['user'] = user_dict.dict()


async def request_context(request: Request):
    # print(id(request))
    """ 保存当前request对象到上下文中 """
    REQUEST_CONTEXT.set(request)
