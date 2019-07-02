from flask import Blueprint
from flask import request, jsonify

from dao_show.home_dao import home_dao
from logger import api_logger
from dao.user_dao import UserDao

blue_home = Blueprint('home_api', __name__)


@blue_home.route('/home/index/', methods=("GET",))
def home_view():
	dao = home_dao()
	# 查询轮播数据
	img_wheel_datas = dao.query_all('wheel')
	# 查询导航的数据
	img_nav_datas = dao.query_all('nav')
	#查询选择列表的数据
	
	img_chosen_datas = dao.query_all('chosen')
	for img_chosen_data in img_chosen_datas:
		img_chosen_category_id = img_chosen_data['trackid']
		print(img_chosen_category_id)
		img_chosen_detail = dao.query_group(img_chosen_category_id,('id','name','detail_name','goods_img','price','marketprice'))

		img_chosen_data['listimg'] = img_chosen_detail

	img_chosen_otherdatas = dao.query_type_nav('id','category_name','category_id')
	print(img_chosen_otherdatas)

	for img_chosen_otherdata in img_chosen_otherdatas:

		img_chosen_categoryid = img_chosen_otherdata['category_id']
		img_chosens = dao.query_group(img_chosen_categoryid,('id','name','detail_name','goods_img','price'))
		img_chosen_otherdata['imglist'] = img_chosens

	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,
		'img_chosen_otherdata':img_chosen_otherdatas
		
	})

@blue_home.route('/home/index/<category_id>/', methods=("GET",))
#导航类列表表详情
def nav_list_view(category_id):
	dao = home_dao()
	nav_datas = dao.query_group(category_id,('name','detail_name','price','marketprice','goods_img'))

	return jsonify({
	    'code': 8000,
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
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': bigimg_eat_datas,
		'img_eat_datas':img_eat_datas
	
	})

@blue_home.route('/detail/<id>/', methods=("GET",))
# 商品详情页面
def detail_view(id):
	dao = home_dao()
	detail_datas = dao.query_detail(('id', 'name', 'detail_name', 'price', 'marketprice',
	                                 'child_id', 'pro_addr'),detail_id=id)
	
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': detail_datas
	})

@blue_home.route('/detail/img/<string:id>/', methods=("GET",))
# 商品图片详情页面
def detail_img_view(id):
	dao = home_dao()
	detail_datas = dao.query_detail(('id', 'detail_img_url'), detail_id=id)
	
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': detail_datas,
	})


@blue_home.route('/type/list/<category_id>/', methods=("GET",))
def type_view(category_id):
	#商品分类
	dao = home_dao()
	type_detail_datas = dao.query_group_all(('id','category_name','child_id','category_id'),arg='category_id')
	
	#获取category_id 分组查询
	if category_id == type_detail_datas[0]['category_id']:
		child_type_detail = dao.query_type_list(('id','child_id','category_id','child_name'),name='category_id',
	                                        id=type_detail_datas[0]['category_id'], typeid='child_name' )
	else:
		child_type_detail = dao.query_type_list(('id', 'child_id', 'category_id','goods_img','child_name'), name='category_id',
		                                        id=category_id, typeid='child_name')
		
	

	return jsonify({
	    'code': 8000,
	    'msg': 'ok',

	    'type_detail_datas': type_detail_datas,
		'child_type_detail':child_type_detail
	})

@blue_home.route('/type/list/child/<child_id>/', methods=("GET",))
	#传入商品的名字 child_id
def type_detail_view(child_id):
	dao = home_dao()
	type_detail = dao.query_name(('id','name','detail_name','price','marketprice','pro_addr','goods_img')
	               ,name_type='child_id',name=child_id)
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
		'type_detail':type_detail

	})

	


	