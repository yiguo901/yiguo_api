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
	print(u_id)
	if u_id:
		dao = cart_dao()
		cart_datas = dao.cart_query(u_id)
		if not cart_datas:
			return jsonify({
				'code': '202',
				'msg': '用户id输入错误'

			})
		
		else:
			s = cart_datas[0]['c_goods_id']
			res = dao.recommend_query(s)[0].get('category_id',None)
			recommends = dao.recommend_datas(res)
			#推荐商品
			for cart_data in cart_datas:
				g_id = cart_data['c_goods_id']
				goods_data = dao.query_goods(('id','name','price','goods_img'),id=g_id)[0]
				cart_data['goods_detail'] = goods_data
	
			return jsonify({
				'code': '200',
				'msg': 'ok',
				'cart_datas': cart_datas,
				'recommends':recommends
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
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	if u_id:
		dao = cart_dao()
		status = dao.query_status(gid,u_id)
		print(u_id,gid)
		if not status:
			dao.add_cart('1', gid, u_id)
			# 购物车数据插入数据库
			print("插入成功！")
			return jsonify({
				'code': 200,
				'msg': '插入成功'
			})
		else:
			goods_num = status.get('c_goods_num')
			dao.update_cart(goods_num + 1, gid, u_id)
			return jsonify({
				'code': 200,
				'msg': '加入数量成功'
			})
	return jsonify({
		'code': '202',
		'msg': '请登录'
	})



@blue_cart.route('/add/address/', methods=('POST',))
def address_view():
	#新增收货地址
	resps = request.get_json().get('data',None)
	print(resps)
	token = request.args.get("token", None)
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	print(u_id)
	if u_id:
	#resp 为一个列表
		if not resps:
			return jsonify({
				'code': '202',
				'msg': '参数error'
			})
		else:
			addr = ','.join([','.join(i.values()) for i in resps])
			result = addr + ',' + str(u_id)
			#tom,123456789,西安市#高新区#高新6路,0,1

			print(result)
			#插入数据address表
			return jsonify({
				'code': '200',
				'msg': '更新地址成功！'
			})
	else:
		return jsonify({
			'code': '202',
			'msg': 'token不正确'
		})


	
	