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
		sql = 'select name,goods_wheel_img,price from goods group by child_id'
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