from flask import Blueprint
from flask import request, jsonify
from logger import api_logger
from dao.user_dao import UserDao

blue_home = Blueprint('home_api', __name__)


@blue_home.route('/home/index/', methods=("GET",))
def home_view():
	dao = UserDao()
	img_wheel_datas = dao.query('ygwheel',page=4)
	img_nav_datas = dao.query('ygnav', page=7)
	img_chosen_datas = dao.query('ygchosen',page=3)
	
	
	
	
	
	
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_wheel': img_wheel_datas,
		'data_nav': img_nav_datas,
		'data_chosen': img_chosen_datas,
	})
	
if __name__ == '__main__':
	dao = UserDao()
	img = dao.query('ygwheel','id','img')

	print(img)
	
	
