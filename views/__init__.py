from views import home_view, cart_view, user_view, order_view
from flask import request


def check_requirments(method="GET", *params):
    # 检查必要参数
    data = request.args if method == "GET" else request.form
    msg = {param: "必须提供"
           for param in params if data.get(param, None) is None}

    return msg