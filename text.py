
from libs.cache import *


if __name__ == '__main__':
	s = new_token()
	print(s)
	res = save_token(s,1)
	p = get_token_user_id('73542f6e007a4bceb93c393e272a4e8e')
	print(res,'**',p)
	
