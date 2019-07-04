# -*- coding: utf-8 -*-
# @Time : 2019/7/2 10:08

from flask import Blueprint
from flask import request, jsonify

from libs import cache
from libs.cache import check_token, get_token_user_id

blue_order = Blueprint('order_api', __name__)


@blue_order.route('/order/', methods=('POST',))
def user_add_order():
    from views import check_requirments
    check_errors = check_requirments("POST",
                                     'token', 'addr_id',
                                     'goods_ids', 'goods_cnt')
    if check_errors:
        return jsonify({
            'code': 202,
            'msg': check_errors
        })

    user_id = cache.get_token_user_id(request.form.get('token'))
    return jsonify({
        'code': 200
    })