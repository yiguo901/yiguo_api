from flask import Blueprint, jsonify, request

from dao_user.mine_dao import MineDao
from libs import cache

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
