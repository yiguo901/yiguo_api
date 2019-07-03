from flask import Blueprint
from flask import request, jsonify

from cart_dao.cartdao import cart_dao
from libs.cache import *


blue_cart = Blueprint('cart_api', __name__)


@blue_cart.route('/cart/show/', methods=('POST',))
def cart_view():
	#将用某用户购物车的信息展示给前端
	token = request.args.get("token", None)
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	if u_id:
		dao = cart_dao()
		cart_datas = dao.cart_query(u_id)
		for cart_data in cart_datas:
			g_id = cart_data['c_goods_id']
			goods_data = dao.query_goods(('id','name','price','goods_img'),id=g_id)
			cart_data['goods_detail'] = goods_data
		return jsonify({
			'code': '202',
			'msg': '请登录',
			'cart_datas': cart_datas
		})
	else:
		return jsonify({
			'code': '202',
			'msg': '请登录'
		})

@blue_cart.route('/cart/add/<string:gid>/', methods=('POST',))
def add_cart_view(gid):
	#商品添加购物车
	# 获取前端传来的商品id 插入cart表
	token = request.args.get("token", None)
	print("*", token)

	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	if u_id:
		dao = cart_dao()
		status = dao.query_status(gid,u_id)
		print(u_id,gid)
		print(status)
		if not status:
			cart_datas = dao.add_cart('1', gid, u_id)
			# 购物车数据插入数据库
			print("插入成功！")
			return jsonify({
				'code': 200,
				'msg': '插入成功'
			})
		else:
			goods_num = status.get('c_goods_num')
			cart_datas = dao.update_cart(goods_num + 1, gid, u_id)
			return jsonify({
				'code': 200,
				'msg': '加入数量成功'
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
