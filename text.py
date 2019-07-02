# from cart_dao.cartdao import cart_dao
from libs.cache import *
# from logger import api_logger
# from dao.user_dao import UserDao

if __name__ == '__main__':
	s = new_token()
	print(s)
	save_token(s,1)
