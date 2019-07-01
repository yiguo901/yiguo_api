from dao import BaseDao


class cart_dao(BaseDao):

    def query(self, table,*fields,):
        sql = 'select {} from {}'.format(table,','.join(*fields))
        print(sql)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data
    
    def query_status(self,u_id):
        sql = 'select * from cart where c_user_id={}'.format(u_id)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data

    def add_cart(self,*fields1):
        sql = 'insert into cart(c_goods_num,c_is_select,c_goods_id,c_user_id)values() '.format(','.join(*fields1))
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data
        

    def cart_list(self):
        pass

