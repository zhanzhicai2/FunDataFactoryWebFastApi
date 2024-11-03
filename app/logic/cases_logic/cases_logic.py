# encoding: utf-8
# @File  : cases_logic.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/10/31

from app.commons.utils.context_utils import REQUEST_CONTEXT
from app.crud.case.CaseDao import CaseDao
from app.crud.operation.OperationDao import LikeOperationDao, CollectionOperationDao


def like_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    result = LikeOperationDao.like(id, user)
    return result


def collection_logic(id: int):
    user = REQUEST_CONTEXT.get().user
    result = CollectionOperationDao.collection(id, user)
    return result


def get_user_groups_logic():
    user = REQUEST_CONTEXT.get().user
    groups = CaseDao.get_user_group_name(user)
    group_list = [id(0) for i in groups]
    return group_list


# 搜索内容
def search_case_logic(search: str):
    user = REQUEST_CONTEXT.get().user
    cases = CaseDao.get_search_case(user, search)
    return cases


# 用例展示
def case_list_logic(page: int = 1, limit: int = 10, show: str = None,
                    project_id: int = None, case_id: int = None):
    user = REQUEST_CONTEXT.get().user
    cases, total = CaseDao.get_all_cases(user, page, limit, show, project_id, case_id)
    cases_lists = dict(total=total, lists=cases)
    return cases_lists
