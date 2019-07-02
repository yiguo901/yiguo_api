from flask import Blueprint
from flask import request, jsonify

from cart_dao.cartdao import cart_dao
from libs.cache import *


blue_cart = Blueprint('cart_api', __name__)


@blue_cart.route('/cart/data/', methods=('POST',))
#临时购物车数据
def cart_view():
	token = request.args.get("token",None)
	cart_datas = request.get_json().get('data')
	print("*",token)
	"""
				{
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
				dao.update_stock(stock - 1,g_id) #更新库存
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
	
@blue_cart.route('/cart/<string:id>/', methods=('POST',))
def cart_add_num(id):
	#获取商品id
	token = request.args.get("token",None)
	#获取前端传来的cart数据
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	#手动添加购物车
	if u_id:
		dao = cart_dao()
		stock = dao.query_stock(id)
		status = dao.query_status(id,u_id)
		print('!!!!!!', status)
		if not status:
			#购物车没有该商品，增加一条记录
			cart_datas = dao.add_cart(1, id, u_id)
			# 购物车数据插入数据库
			print("插入成功！")
			return jsonify({
				'code': 8000,
				'msg': '插入成功'
			})
		else:
			if stock:
				goods_num = status[0].get('c_goods_num')
				cart_datas = dao.update_cart(goods_num + 1, id, u_id)
				return jsonify({
					'code': 8000,
					'msg': '加入数量成功'
				})
			else:
				return jsonify({
					'code': 8001,
					'msg': '库存不足'
				})
				
	return jsonify({
		'code': '202',
		'msg': '请登录',
	})

@blue_cart.route('/cart/change_num/<string:id>/<string:num>/', methods=('POST',))
def cart_add(id,num):
	#id为商品id
	#num=1 商品增加一件 num=0 商品减少一件
	token = request.args.get("token",None)
	print("*",token)
	#获取前端传来的cart数据
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	dao = cart_dao()
	status = dao.query_status(id,u_id)
	print(status)
	print('!!!!!!', status)
	if num == '1':
		goods_num = status[0].get('c_goods_num')
		cart_datas = dao.update_cart(goods_num + 1,id,u_id)
		return jsonify({
			'code': '203',
			'msg': '增加商品一件',
		})
	elif num == '0':
		goods_num = status[0].get('c_goods_num')
		print(goods_num)
		print(goods_num - 1)
		cart_datas = dao.update_cart(goods_num - 1,id,u_id)
		goods_num = status[0].get('c_goods_num')
		if goods_num == 0:
			#当商品数量为0 则删除数据
			result = dao.del_cart_goods(id, u_id)
		return jsonify({
			'code': '203',
			'msg': '减少商品一件',
		})
	print("插入成功！")
	return jsonify({
		'code': 8000,
		'msg': '插入成功'
	})

@blue_cart.route('/cart/del/<string:id>/', methods=('POST',))
#删除商品
def cart_del_view(id):
	token = request.args.get("token",None)
	print("*",token)
	#获取前端传来的cart数据
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	dao = cart_dao()
	u_id = get_token_user_id(token)
	result = dao.del_cart_goods(id,u_id)
	print(result)
	return jsonify({
		'code': 8000,
		'msg': '删除成功！'
	})




@blue_cart.route('/cart/show/', methods=('POST',))
def cart_show():
	token = request.args.get("token",None)
	print("*",token)
	#获取前端传来的cart数据
	if token is None:
		return jsonify({"code": 201, "msg": "token查询参数必须提供"})
	u_id = get_token_user_id(token)
	dao = cart_dao()
	goods_datas = dao.fund_cart(u_id)
	print("&&&",goods_datas)
	goods_lists = []
	for goods_data in goods_datas:
		g_id = goods_data['c_goods_id']
		g_num = goods_data['c_goods_num']
		goods = dao.query_goods(('id','name','price','goods_img'),id=g_id)[0]
		goods['goods_num'] = g_num
		goods_lists.append(goods)
	print("****",goods_lists)
	#算总价
	prices = 0
	for goods_list in goods_lists:
		prices += goods_list['price']*goods_list['goods_num']
	datas = {}
	datas['prices'] = '%.2f'%(prices)
	datas['goods_show'] = goods_lists
	
	
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'goods_datas':datas
	})

	
	
	
	
	




if __name__ == '__main__':
	s = new_token()
	print(s)
	save_token(s,1)
	# token = 0cbca629c7054578b56ec58897807129
	#userID = 1
