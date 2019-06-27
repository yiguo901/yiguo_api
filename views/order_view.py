from flask import Blueprint, request, jsonify

from libs import cache

blue_order = Blueprint('order_api',__name__)


@blue_order('/order/',methods=('POST',))
def order_view():
    # 验证登录
    token = request.args.get('token', None)
    if token is None:
        return jsonify({
            'code': 202,
            'msg': '获取token失败'
        })
    if cache.check_token(token):
        user_id = cache.get_token_user_id(token)
        ord_unm= ''

    return jsonify({
        'code': 200,
        'msg': 'ok',
        'data': {
            'user_id': user_id,
            'ord_num': '',
            'status': '',
            'price': '',
        }
    })