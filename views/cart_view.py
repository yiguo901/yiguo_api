from flask import Blueprint
from flask import request, jsonify
from logger import api_logger
from dao.user_dao import UserDao

blue_cart = Blueprint('cart_api', __name__)


@blue_cart.route('/cart/', methods=('POST', 'GET'))
def cart_view():
	pass