from flask import Blueprint
from flask import request, jsonify

from cart_dao.cartdao import cart_dao
from libs.cache import *
from logger import api_logger
from dao.user_dao import UserDao

blue_cart = Blueprint('cart_api', __name__)


@blue_cart.route('/cart/', methods=('POST',))
def cart_view():
	token = request.args.get("token", None)

	g_num = request.get_json("goods_num")  # 获取商品的数量
	g_id = request.get_json("goods_id")  # 获取商品的id
	print('**', token, g_num, g_id)
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	if u_id:
		dao = cart_dao()
		u_status = dao.query_status(u_id)
		if not u_status:
			cart_datas = dao.add_cart(g_num, 'True', g_id, u_id)
			#购物车数据插入数据库
			
			
			
			
		
	


if __name__ == '__main__':
	s = new_token()
	print(s)
	save_token(s,1)
	# token = 0cbca629c7054578b56ec58897807129
	#userID = 1
