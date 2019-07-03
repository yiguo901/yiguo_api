from dao import BaseDao


class home_dao(BaseDao):

	def query_eat(self,):
		sql = 'select eat_content, eat_img from ygeat where id<53 '
		data = self.query(sql)
		return data
	def query_eat_limit(self):
		sql = 'select eat_content, eat_img, eat_time  from ygeat  where id>53 '
		data = self.query(sql)
		return data
		
	def query_all(self, table):
		sql = 'select * from %s' %(table)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_all_limit(self, table):
		sql = 'select * from %s limit 4' %(table)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data

	def query_group(self, child_id,*fields, page=4):

		sql = 'select {} from goods where category_id={} limit {}'.format(','.join(*fields), child_id,page)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def query_detail(self, *fields,detail_id):
		sql = 'select {} from goods where id={} '.format(','.join(*fields),detail_id)
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def query_type_detail_all(self, *fields,name,id):
		sql = 'select %s from goods where %s=%s ' %(','.join(*fields),name,id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def query_name(self, *fields,name_type,name,type):
		#二级分类
		sql = 'select {} from goods where {}={} order by {}'.format(','.join(*fields), name_type, name,type)
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def query_category_nav(self,*fields,category_id):
		sql = 'select {} from goods where category_id={}'.format(','.join(*fields), category_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
		
	def query_category(self):
		sql = 'select * from category '
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	
	def query_child(self,category_id):
		sql = 'select child_name,child_id,child_img from child where category_id={}'.format(category_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
		
	def welfare_query(self,category_id):
		sql = 'select id,name,detail_name,goods_img,price from goods where category_id={} limit 4'.format(category_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def hot_query(self, *fields):
		sql = 'select {} from goods order by sale '.format(','.join(*fields))
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data

# # 分类显示
	# def query_group_all(self, *fields, arg):
	# 	# 第一个传入元组，第二个传入关键字
	# 	sql = 'select {} from  goods group by {}'.format(','.join(*fields), arg)
	# 	print(sql)
	# 	with self.db as c:
	# 		c.execute(sql)
	# 		data = c.fetchall()
	# 		return data
	#
	# def query_type_list(self, *fields, name, id, typeid):
	# 	sql = 'select {} from  goods where {}={}  group by {}'.format(','.join(*fields), name, id, typeid)
	# 	with self.db as c:
	# 		c.execute(sql)
	# 		data = c.fetchall()
	# 	return data
	#
	# def query_type(self):
	# 	sql = 'select id,category_name,category_id from goods group by category_id'
	# 	with self.db as c:
	# 		c.execute(sql)
	# 		data = c.fetchall()
	# 		return data
	#
	# def query_type_nav(self, *fields):
	# 	sql = 'select %s from goods group by category_id' % (','.join(fields))
	# 	print(sql)
	# 	with self.db as c:
	# 		c.execute(sql)
	# 		data = c.fetchall()
	# 		return data

# if __name__ == '__main__':
# 	dao = home_dao()
# 	type_detail = dao.query_name(('id','name','detail_name','price','marketprice','pro_addr','goods_img')
# 	               ,name_type='child_name',name='\'苹果\'')
# 	# home_dao().query_group(1001,('id', ))

