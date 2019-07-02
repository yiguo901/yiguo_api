from flask import Blueprint
from flask import request, jsonify

from cart_dao.cartdao import cart_dao
from libs.cache import *


blue_cart = Blueprint('cart_api', __name__)


@blue_cart.route('/cart/show/', methods=('POST',))
#临时购物车数据
def cart_view():
	token = request.args.get("token",None)
	cart_datas = request.get_json().get('data')
	print("*",token)
	"""
				{
				"total_price":100,
				"data":[
					{
					"goods_num":1,
					"goods_id":1
				},
				{
					"goods_num":2,
					"goods_id":3
				}
				]
			}
	"""
	#获取前端传来的cart临时数据json
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	if u_id:
		dao = cart_dao()
		for cart_data in cart_datas:
			
			g_num = cart_data.get('goods_num')
			g_id = cart_data.get('goods_id')
			status = dao.query_status(u_id, g_id)
			stock = dao.query_stock(g_id)
			print('!!!!!!', status)
			if not status:
				cart_datas = dao.add_cart(g_num, g_id, u_id)
				# 购物车数据插入数据库
				print("插入成功！")
				return jsonify({
					'code': 8000,
					'msg': '插入成功'
				})
				
			else:
				goods_num = status[0].get('c_goods_num')
				if stock:
					cart_datas = dao.update_cart(goods_num + 1, id, u_id)
					return jsonify({
						'code': 8000,
						'msg': '加入数量成功'
					})
				else:
					return jsonify({
						'code': 8001,
						'msg': '库存不足！'
					})
		return jsonify({
			'code': '202',
			'msg': '请登录',
		})
	

if __name__ == '__main__':
	s = new_token()
	print(s)
	save_token(s,1)
	# token = 0cbca629c7054578b56ec58897807129
	#userID = 1
