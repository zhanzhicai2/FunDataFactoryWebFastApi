# encoding: utf-8
# @File  : cases_api.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/11/01


from app.logic.cases_logic import cases_logic
from app.commons.responses.response_model import ResponseDto, ListResponseDto
from app.routers.cases.request_model.cases_in import AddCasesParams, EditCasesParmas, RunBody


def like(id: int):
    result = cases_logic.like_logic(id)
    return ResponseDto(msg="点赞成功" if result else "取消点赞成功")


def collection(id: int):
    result = cases_logic.collection_logic(id)
    return ResponseDto(msg="收藏成功" if result else "取消收藏成功")


# 动态获取业务线分组
def get_user_groups():
    groups = cases_logic.get_user_groups_logic()
    return ResponseDto(data=groups)


# 模糊搜索用例
def search_case(search: str):
    cases = cases_logic.search_case_logic(search)
    return ResponseDto(data=cases)


# 用例展示
def case_list(page: int = 1, limit: int = 10, show: str = None,
              project_id: int = None, case_id: int = None):
    cases_lists = cases_logic.case_list_logic(page, limit, show, project_id, case_id)
    return ListResponseDto(data=cases_lists)


# 用例详情展示
def case_detail(id: int):
    case = cases_logic.case_detail_logic(id)
    return ResponseDto(data=case)


# 添加参数组合
def add_params(body: AddCasesParams):
    cases_logic.add_params_logic(body)
    return ResponseDto(msg="新增参数组合成功")


# 编辑参数组合
def edit_params(body: EditCasesParmas):
    cases_logic.edit_params_logic(body)
    return ResponseDto(msg="编辑参数组合成功")


# 删除参数组合
def delete_params(id: int):
    cases_logic.delete_params_logic(id)
    return ResponseDto(msg="删除参数组合成功")


# 参数组合列表
def get_cases_params(cases_id: int, page: int, limit: int):
    params_list = cases_logic.get_cases_params_logic(cases_id, page, limit)
    return ResponseDto(data=params_list)


# 运行造数场景
def plat_run(body: RunBody):
    run_data = cases_logic.plat_run_logic(body)
    return ResponseDto(msg="运行成功", data=run_data)


# 运行日志列表
def log_list(page: int = 1, limit: int = 20, group: str = None, project: str = None,
             requests_id: str = None, search: str = None, call_type: str = None, run_status: str = None):
    log_list = cases_logic.log_list_logic(page, limit, group, project, requests_id, search, call_type, run_status)
    return ListResponseDto(data=log_list)


# 外部调用运行造数场景
def out_run(id: int):
    run_data = cases_logic.out_run_logic(id)
    return ResponseDto(msg="运行成功", data=run_data)


# rpc调用运行造数场景
def rpc_run(method: str, data: dict):
    run_data = cases_logic.rpc_run_logic(method, data)
    return ResponseDto(msg="运行成功", data=run_data)
