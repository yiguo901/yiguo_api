from dao import BaseDao


class cart_dao(BaseDao):

    def query_goods(self, *fields, id):
        #查询购物车数据 根据u_id 查询商品信息
        
        sql = 'select {} from goods where id={} limit 1'.format(','.join(*fields),id)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data
    
    def query_status(self,id,u_id):

        sql = 'select c_goods_num from cart where c_goods_id={} and c_user_id={} limit 1'.format(id,u_id)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        if data:
            return data
        else:
            return False
        
    def query_status_(self,u_id):

        sql = 'select c_goods_num from cart where c_user_id={} limit 1'.format(u_id)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        if data:
            return data
        else:
            return False

    def add_cart(self,c_goods_num,c_goods_id,c_user_id):
        sql = 'insert into cart(c_goods_num,c_is_select,c_goods_id,c_user_id)values({},1,{},{})'.format(c_goods_num,c_goods_id,c_user_id)
        print(sql)
        with self.db as c:
            c.execute(sql)
        return True
    
    def update_cart(self,c_goods_num,c_goods_id,c_user_id):
        sql = 'update cart set  c_goods_num={} where c_goods_id={} and c_user_id={}'.format(c_goods_num,c_goods_id,c_user_id)
        print(sql)
        with self.db as c:
            c.execute(sql)
        return True

    def del_cart_goods(self,c_goods_id,c_user_id):
        sql = 'delete from cart where c_goods_id={} and c_user_id={}'.format(c_goods_id,c_user_id)
        print(sql)
        with self.db as c:
            c.execute(sql)
        return True
    
    def fund_cart(self,u_id):
    
        sql = 'select c_goods_id,c_goods_num from cart where c_user_id={}'.format(u_id)
        print(sql)
        with self.db as c:
            c.execute(sql)
            data = c.fetchall()
        return data
    
    def query_stock(self, id):
        sql = 'select stock from goods where id={} '.format(id)
        print(sql)
        with self.db as c:
            c.execute(sql)
            data = c.fetchone()
        return data['stock']
    
    def update_stock(self,stock, id):
        sql = 'update goods set stock={} where id={}'.format(stock, id)
        print(sql)
        with self.db as c:
            c.execute(sql)
            data = c.fetchone()
        return True
        
        

        
if __name__ == '__main__':
    dao = cart_dao()
    print(dao.query_stock(1))
    