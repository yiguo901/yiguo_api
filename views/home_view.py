from flask import Blueprint
from flask import request, jsonify

from dao_show.home_dao import home_dao

blue_home = Blueprint('home_api', __name__)


@blue_home.route('/home/index/', methods=("GET",))
def home_view():
	dao = home_dao()
	# 查询轮播数据
	img_wheel_datas = dao.query_all('wheel')
	# 查询导航的数据
	img_nav_datas = dao.query_all('nav')
	#查询选择列表的数据
	
	img_chosen_datas = dao.query_all_limit('chosen')
	for img_chosen_data in img_chosen_datas:
		img_chosen_category_id = img_chosen_data['trackid']
		img_chosen_detail = dao.query_group(img_chosen_category_id,('id','name','detail_name','goods_img','price','marketprice'))
		img_chosen_data['listimg'] = img_chosen_detail
	other_chosen_datas = dao.query_category()
	for other_chosen_data in other_chosen_datas:
		type_id = other_chosen_data['category_id']
		img_chosens = dao.query_group(type_id,('id','name','detail_name','goods_img','price','marketprice'))
		other_chosen_data['imglist'] = img_chosens

	return jsonify({
		'code': 200,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,  #4条数据
		'img_chosen_otherdata':other_chosen_datas  # 12个分类

	})

@blue_home.route('/home/index/nav/<category_id>/', methods=("GET",))
#导航类列表表详情
def nav_list_view(category_id):
	dao = home_dao()
	nav_datas = dao.query_category_nav(('id','name','detail_name','price','marketprice','goods_img'),category_id=category_id)

	return jsonify({
	    'code': 200,
	    'msg': 'ok',
	    'data_nav': nav_datas,
	
	})

@blue_home.route('/home/eat/', methods=("GET",))
# 吃饭吧详情
def eat_view():
	dao = home_dao()
	bigimg_eat_datas = dao.query_eat()
	img_eat_datas = dao.query_eat_limit()
	
	return jsonify({
	    'code': 200,
	    'msg': 'ok',
	    'data_wheel': bigimg_eat_datas,
		'img_eat_datas':img_eat_datas
	})

@blue_home.route('/detail/<id>/', methods=("GET",))
# 商品详情页面
def detail_view(id):
	dao = home_dao()
	detail_datas = dao.query_detail(('id', 'name', 'detail_name', 'price', 'marketprice',
	                                 'child_id', 'pro_addr','goods_wheel_img'),detail_id=id)
	
	return jsonify({
	    'code': 200,
	    'msg': 'ok',
	    'data_wheel': detail_datas
	})

@blue_home.route('/detail/img/<string:id>/', methods=("GET",))
# 商品图片详情页面
def detail_img_view(id):
	dao = home_dao()
	detail_datas = dao.query_detail(('id', 'detail_img_url'), detail_id=id)
	
	return jsonify({
	    'code': 200,
	    'msg': 'ok',
	    'data_wheel': detail_datas,
	})

@blue_home.route('/type/list/<category_id>/', methods=("GET",))
def type_view(category_id):
	#商品分类
	#1001
	dao = home_dao()
	#查询大类商品
	category_datas = dao.query_category()
	if category_id == category_datas[0]['category_id']:
		child_datas = dao.query_child(category_datas[0]['category_id'])
	else:
		child_datas = dao.query_child(category_id)

	return jsonify({
	    'code': 200,
	    'msg': 'ok',
	    'type_detail_datas': category_datas,
		'child_type_datas':child_datas
	})

@blue_home.route('/type/list/child/<child_id>/<string:id>/', methods=("GET",))
	#二级分类，传入商品的名字 child_id
def type_detail_view(child_id,id):
	#id=0 销量排序 id=1 新品排序 id=2价格排序
	dao = home_dao()
	if id == '0':
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='child_id', name=child_id, type='sale')
	elif id == '1':
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='child_id', name=child_id,type='stock')
	else:
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='child_id', name=child_id,type='price')
	
	return jsonify({
	    'code': 200,
	    'msg': 'ok',
		'type_detail':type_detail

	})

@blue_home.route('/home/card/', methods=("GET",))
def free_card_view():
	#home页面的会员页面
	dao = home_dao()
	free_cards = dao.query_type_detail_all(('id','child_name','name','detail_name','price','goods_img'),name='category_id',id='2001')
	return jsonify({
	    'code': 200,
	    'msg': 'ok',
		'img_datas':free_cards
	})

@blue_home.route('/home/welfare/<string:id>/',methods=("GET",))
def welfare_view(id):
	#福利页面
	dao = home_dao()
	if id == '0':
		welfare_datas=dao.welfare_query('1003')
	elif id == '1':
		welfare_datas = dao.welfare_query('1006')
	else:
		welfare_datas = dao.welfare_query('1008')
		
	return jsonify({
		'code': 200,
		'msg': 'ok',
		'datas1': welfare_datas[0],
		'datas2':welfare_datas[1]
	})

@blue_home.route('/home/new/',methods=("GET",))
def new_view():
	#新品上市
	dao = home_dao()
	datas = dao.query_type_detail_all(('id','name','detail_name','price','goods_img')
	                          ,name='is_chosen',id='1')
	l = int(len(datas) / 2)
	
		
	return jsonify({
		'code': 200,
		'msg': 'ok',
		'datas':datas[:l],
		'datas_o':datas[l:]
	})


@blue_home.route('/home/hot/',methods=("GET",))
#人气美食
def hot_view():
	dao = home_dao()
	datas = dao.hot_query(('id','name','detail_name','price','goods_img'))

	return jsonify({
		'code': 200,
		'msg': 'ok',
		'datas':datas[:6],
		'datas_o':datas[6:]
	})


@blue_home.route('/home/nav/<string:category_id>/<string:id>/',methods=("GET",))
def nav_view(id,category_id):
	#/ home / nav / < string: category_id > /
	#/home/nav/<string:category_id>/?id=1
	#/home/nav/<string:category_id>/?id=2
	
	dao = home_dao()
	#当id=0 按销量排序
	#当id=1 按精选排序
	#其他按价格排序
	if id == '0':
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='category_id', name=category_id, type='sale')
	elif id == '1':
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='category_id', name=category_id, type='is_chosen')
	else:
		type_detail = dao.query_name(('id', 'name', 'detail_name', 'price', 'marketprice', 'pro_addr', 'goods_img')
		                             , name_type='category_id', name=category_id, type='price')
	return jsonify({
		'code': 200,
		'msg': 'ok',
		'datas':type_detail
	})
