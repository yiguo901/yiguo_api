from flask import Blueprint
from flask import request, jsonify
from logger import api_logger
from dao.user_dao import UserDao

blue2 = Blueprint('home_api', __name__)


@blue2.route('/home/index/', method=("GET",))
def home_view():
	dao = UserDao()
	img_data = dao.query('ygwheel', ('id', 'img'))
	
	
	
	return jsonify({
		'code': 8000,
		'msg': 'ok',
		'data_img': img_data,
		'data_wheel':img_data
	})



