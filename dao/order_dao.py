# -*- coding: utf-8 -*-
# @Time : 2019/7/2 10:04

# 新增订单
from dao import BaseDao
from dao.user_dao import UserDao



class Order_Dao(BaseDao):

    def save(self, **values):
            return super(Order_Dao, self).save('orders', **values)

    def add_detail(self, o_order_id,o_goods_id,o_goods_num):
            sql = 'insert into orderdetail(o_order_id,o_goods_id,o_goods_num,)values{}'.format(o_order_id,
                                                                                               o_goods_id,
                                                                                               o_goods_num)
            with self.db as c:
                c.execute(sql)
            return True

    def goods_by_id(self,goods_id):
        sql = 'select name, price, goods_img from goods where id=%s'
        result = self.query(sql, goods_id)
        if result:
            return result[0]
        return None

    # 显示订单
    def show_orders(self,user_id):
        sql = 'select * from orders where user_id = %s'
        order_list = self.query(sql, user_id)
        return order_list


    # 修改订单状态

    def to_update_order(self,o_status,user_id,id):
        sql = "UPDATE orders set o_status=%s where user_id=%s and id=%s"
        updata_order = self.query(sql,o_status)

    def get_order_id(self):
        sql = "select last_insert_id from orders"
        res = self.query(sql)


    # 取消订单
    def delete_order(self,id,user_id):
        sql = "delete from orders where id=%s and user_id=%s"
        del_order = self.query(sql, id, user_id)


    def query_user_sale(self,u_id):
        sql = "select balance from users where id=%s"
        res = self.query(sql, u_id)
        return res

    # 评价
    # def user_comment(self,user_id,order_id):
    #     return super(Order_Dao, self).search_all("comment", where="user_id", args=user_id, page=1,
    #                                            page_size=5)

    # 获取商铺评论
    # def shop_pl(self,v_shop_id):
    #     sql = 'select * from valuetion where v_shop_id = %s'
    #     user_profile = self.query(sql, v_shop_id)
    #     return user_profile


if __name__ == '__main__':
    data = Order_Dao().user_comment(3)
    print(data)