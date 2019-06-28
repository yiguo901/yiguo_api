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
	def query_type(self,page=1):
		sql = 'select name,goods_wheel_img,price from goods group by child_id limit %s'%(page)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
	
	
	# def list(self, table_name,
	#          *fields, where=None, args=None,
	#          page=1, page_size=20):
	# 	if not fields:
	# 		fields = "*"
	# 	if not where:
	# 		sql = "select %s from %s limit %d, %d" % (
	# 			",".join(fields), table_name, (page - 1) * page_size, page_size
	# 		)
	# 	else:
	# 		sql = "select %s from %s where %s = %s limit %d, %d" % (
	# 			",".join(fields), table_name, where, args, (page - 1) * page_size, page_size
	# 		)
	# 	with self.db as c:
	# 		c.execute(sql)
	# 		return list(c.fetchall())
	#
	def query_nav(self, table, child_id):
		sql = 'select name,detail_name,goods_wheel_img,price,marketprice from '\
		      '%s group by %s'%(table, child_id)
		with self.db as c:
			c.execute(sql)
			data = c.fetchall()
			return data
