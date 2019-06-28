from flask import Blueprint
from flask import request, jsonify

from dao_show.home_dao import home_dao
from logger import api_logger
from dao.user_dao import UserDao

blue_home = Blueprint('home_api', __name__)


@blue_home.route('/home/index/', methods=("GET",))
def home_view():
	dao = home_dao()
	img_wheel_datas = dao.query_all('wheel')
	img_nav_datas = dao.query_all('nav')
	img_chosen_datas = dao.query_all('chosen')

	# 查询导航的数据
	# 导航详情列表
	for img_chosen_data in img_chosen_datas:
		nav_trackid = img_chosen_data['trackid']
		nav_groups = dao.query_group('goods',nav_trackid)
		for nav_group in nav_groups:
			img_group = nav_group['goods_wheel_img'].split('#')
			nav_group['goods_wheel_img'] = img_group[0]
		img_chosen_data['imglist'] = nav_groups
	#导航的另一种结构
	nav_type_details = dao.query_type_nav()
	print(")))",nav_type_details)
	for nav_type_detail in nav_type_details:
		nav_type_category_id = nav_type_detail['category_id']
		nav_type_lists = dao.query_group('goods',nav_type_category_id,8)
		for nav_type_list in nav_type_lists:
			img_group = nav_type_list['goods_wheel_img'].split('#')
			nav_type_list['goods_wheel_img'] = img_group[0]
	
		nav_type_detail['imglist'] = nav_type_lists
		

	
	
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,
		'data_nav_type':nav_type_details
		# 'goodlist':goodlist,
	})

@blue_home.route('/home/index/<child_id>/',methods=("GET",))
#导航类列表表详情
def nav_view(child_id):
	dao = home_dao()





@blue_home.route('/home/index/<child_id>/', methods=("GET",))

def nav_list_view(child_id):
	dao = home_dao()
	nav_datas = dao.query_group('goods', child_id)
	
	for detail_data in nav_datas:
		img = detail_data['goods_wheel_img'].split('#')
		detail_data['goods_wheel_img'] = img[0]
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': nav_datas,
	
	})


@blue_home.route('/home/eat/', methods=("GET",))
# 吃饭吧详情
def eat_view():
	dao = home_dao()
	img_eat_datas = dao.query_all('ygeat')
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': img_eat_datas,
	
	})


@blue_home.route('/detail/<child_id>/', methods=("GET",))
# 商品详情页面
def detail_view(child_id):
	dao = home_dao()
	detail_datas = dao.query_detail(child_id)
	for detail_data in detail_datas:
		img = detail_data['goods_wheel_img'].split('#')
		detail_data['goods_wheel_img'] = img[0]
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': detail_datas,
	
	})


@blue_home.route('/detail/img/<string:id>/', methods=("GET",))
# 商品图片详情页面
def detail_img_view(id):
	dao = home_dao()
	detail_datas = dao.query_detail(id)
	
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': detail_datas,
	
	})


@blue_home.route('/type/<num>/', methods=("GET",))
def type_view(num='1001'):
	dao = home_dao()
	type_datas = dao.query_type()
	
	if num == '1001':
		type_category_id = type_datas[0]['category_id']
		type_detail_datas = dao.query_group_all('goods', type_category_id)
		for type_detail_data in type_detail_datas:
			img = type_detail_data['goods_wheel_img'].split('#')
			type_detail_data['goods_wheel_img'] = img[0]
	else:
		type_detail_datas = dao.query_group_all('goods', num)
		for type_detail_data in type_detail_datas:
			img = type_detail_data['goods_wheel_img'].split('#')
			type_detail_data['goods_wheel_img'] = img[0]

	print(type_datas)
	
	return jsonify({
	    'code': 8000,
	    'msg': 'ok',
	    'data_wheel': type_datas,
	    'type_detail_datas': type_detail_datas
	
	})



