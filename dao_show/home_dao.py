from dao import BaseDao


class home_dao(BaseDao):
	
	def query_eat(self,table):
		sql = 'select * from %s'
		data = self.query(sql, table)
		return data
	
	def query_all(self, table):
		sql = 'select * from %s' % (table)
		
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_type(self):
		sql = 'select id,category_name,category_id from goods group by category_id'
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_type_nav(self,*fields):
		sql = 'select %s from goods group by category_id'%(','.join(fields))
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	
	def query_group(self, child_id,*fields, page=8):

		sql = 'select {} from goods where category_id={} limit {}'.format(','.join(*fields), child_id,page)
		print("***",sql)
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
	
		
	# 分类显示
	def query_group_all(self, *fields, arg):
		# 第一个传入元组，第二个传入关键字
		sql = 'select {} from  goods group by {}'.format(','.join(*fields), arg)
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_type_list(self,*fields, name, id, typeid):
		sql = 'select {} from  goods where {}={}  group by {}'.format(','.join(*fields),name, id, typeid)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	
	def query_name(self, *fields,name_type,name):
		#二级分类
		sql = 'select {} from goods where {}={}'.format(','.join(*fields), name_type, name)
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
		
		
		
# if __name__ == '__main__':
# 	dao = home_dao()
# 	type_detail = dao.query_name(('id','name','detail_name','price','marketprice','pro_addr','goods_img')
# 	               ,name_type='child_name',name='\'苹果\'')
# 	# home_dao().query_group(1001,('id', ))

