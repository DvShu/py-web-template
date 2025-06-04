import math

MSG_CODE = {
    0: "ok",
    10001: "微信验签失败",
    10002: "参数错误",
    10003: "应用APP限制使用",
    10004: "密码错误",
    10005: "账号已过期",
    10006: "用户已封禁",
    10007: "该应用禁止登录",
}


def json(code=0, msg="", data={}, pagination=None, extra=None):
    """
    生成标准JSON格式的响应数据

    Args:
        code (int): 状态码，默认为0表示成功
        msg (str): 提示信息，默认为空字符串
        data (dict): 返回数据，默认为空字典
        pagination (dict|None): 分页信息，包含total/page/page_size字段
        extra (Any|None): 额外数据

    Returns:
        dict: 包含code/msg/data的标准响应结构，data中可能包含分页信息和额外数据
    """
    res = {}
    res["code"] = code
    res["msg"] = msg or MSG_CODE.get(code, "未知错误")
    data_res = {"data": data}
    if pagination:
        data_res["pagination"] = page_response(
            pagination["total"], pagination["page"], pagination["page_size"]
        )
    if extra:
        data_res["extra"] = extra
    res["data"] = data_res
    return res


def page_response(total, page=1, page_size=10):
    total_page = math.ceil(total / page_size)
    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_page": total_page,
        "is_end": page >= total_page,
    }
