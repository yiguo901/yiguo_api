from flask import Blueprint, jsonify, request

from dao.mine_dao import MineDao
from libs import cache
from libs.cache import get_token_user_id

mine_blue = Blueprint("mine_blue", __name__)


@mine_blue.route("/status/", methods=["GET", "POST"])
def oders():
    resp = request.get_json()
    if resp:
        token = resp.get('token')
        user_id = cache.get_token_user_id(token)
        dao = MineDao()
        data = dao.mine_query(user_id)
        if data:
            return jsonify({
                'code': 200,
                'msg': 'ok',
                'data': data
             })
    return jsonify({
        'code': 201,
        'msg': '请求数据失败',
    })


@mine_blue.route("/add/money/", methods=("POST",))
def add_view():
    token = request.args.get("token", None)
    num_money = request.form.get('num_money')
    
    if token is None:
        return jsonify({"code": 201, "msg": "token查询参数必须提供"})
    u_id = get_token_user_id(token)
    dao = MineDao()
    
    bal = dao.query_balance(u_id)
    num = int(bal) + int(num_money)

    dao.add_balance(num, u_id)
    return jsonify({"code": 200, "msg": "充值成功！", "data": num})