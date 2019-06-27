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
	print('***',img_nav_datas)
	# for img_dict in img_nav_datas:
	img_chosen_datas = dao.query_all('chosen')
	type_detail = dao.query_type()
	for type in type_detail:
		img = type['goods_wheel_img'].split('#')
		type['goods_wheel_img']=img[0]
		
		
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,
		'data_type':type_detail
		
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

	

if __name__ == '__main__':
	dao = UserDao()
	img = dao.query('wheel','id','img')

	print(img)