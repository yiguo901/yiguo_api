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

	

	type = img_nav_datas['trackid']
	img_tpye_datas = dao.query_limit('goods',('name','goods_wheel_img','price'),page=8)
	for type_img_data in img_nav_datas:
		type_img = type['goods_wheel_img'].split('#')
		type_img_data['goods_wheel_img'] = type_img[0]
		
	goodlist = []
	for nav in img_nav_datas:
		for i in range(8):
			nav['imgnext'] = img_tpye_datas[i]
			goodlist.append(nav)
		
	type_detail = dao.query_type(page=8)
	for type in type_detail:
		img = type['goods_wheel_img'].split('#')
		type['goods_wheel_img'] = img[0]
		
		
	img_chosen_datas = dao.query_limit(('id','img, trackid'), 'choosen')
	list_img = []
	list_img_datas = dao.query_type(page=6)
	for list_img_data in list_img_datas:
		img = list_img_data['goods_wheel_img'].split('#')
		list_img_data['goods_wheel_img'] = img[0]
	list_img.append(list_img_datas)
	for img_chosen_data in img_tpye_datas:
		for img in range(len(list_img)):
			img_nav_datas['imgtext'] = list_img[img]
			
		
	

		
		
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,
		'data_type':type_detail,
		'goodlist':goodlist,
		
		
		
	})

@blue_home.route('/home/index/<child_id>/',methods=("GET",))
def nav_view(child_id):
	dao = home_dao()
	nav_datas = dao.query_nav('goods',child_id)
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': nav_datas,
		
	})
	
@blue_home.route('/home/eat/', methods=("GET",))
def eat_view():
	dao = home_dao()
	img_eat_datas = dao.query_all('ygeat')
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_eat_datas,
		
	})

@blue_home.route('/detail/<child_id>/',methods=("GET",))
def detail_view(child_id):
	dao = home_dao()
	detail_datas = dao.query_limit(('name','goods_wheel_img',
	                                'price','pro_addr','sale',
	                                'stock','goods_wheel_img'),'goods',page=1)
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': detail_datas,
		
	})


@blue_home.route('/detail/img/<string:id>/', methods=("GET",))
def detail_img_view(id):
	dao = home_dao()
	detail_datas = dao.query_limit(('detail_img_url'), 'goods', page=1)
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': detail_datas,
		
	})
	
	
	

	

if __name__ == '__main__':
	dao = UserDao()
	img = dao.query('wheel','id','img')

	print(img)