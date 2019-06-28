from dao import BaseDao


class home_dao(BaseDao):
	
	def query_limit(self, table,*fields, page=1):
		if not len(fields):
			sql = 'select * from %s limit %s' % (table, page)
		else:
			sql = 'select %s from %s limit %s' % (','.join(fields), table,page)
			print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
		
	def query_args(self, table, *fields):
		if not len(fields):
			sql = 'select * from %s' % (table)
		else:
			sql = 'select %s from %s' % (','.join(fields), table)
		print(sql)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data

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
	def query_type_nav(self):
		sql = 'select id,category_name,category_id from goods group by category_id'
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	
	def query_group(self, table, child_id, page=8):
		sql = 'select name,detail_name,goods_wheel_img,price,marketprice from '\
		      '%s where category_id=%s limit %s'%(table, child_id,page)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_group_all(self, table, child_id):
		sql = 'select name,detail_name,goods_wheel_img,price,marketprice from '\
		      '%s where category_id=%s'%(table, child_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	def query_detail(self, detail_id):
		sql = 'select name,detail_name,goods_wheel_img,price,marketprice from goods'\
		      ' where id=%s limit 1' %(detail_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
