from dao import BaseDao
from logger import api_logger


class MineDao(BaseDao):



    def mine_query(self,user_id):
        try:
            # 余额
            balance = self.list('users', ('balance'),
                                where='id',args=user_id)
            # 待支付
            o_status = self.list('orders', ('o_user_id', 'o_time', 'o_price'),
                                 where='o_status', args=0, page=1, page_size=5)
            # 待收货
            dispatched = self.list('orders', ('o_user_id', 'o_time', 'o_price'),
                                 where='o_status', args=1, page=1, page_size=5)
        #   待评价
            to_be_evaluated = self.list('orders', ('o_user_id', 'o_time', 'o_price'),
                                 where='o_status', args=2, page=1, page_size=5)
        #   全部订单
            all_orders = self.list('orders', ('o_user_id', 'o_time', 'o_price'),
                                 where='o_status', page=1, page_size=5)


        #

        except Exception as e:
            raise Exception({'code': 201, 'msg': e})

        return {
            "balance": balance,
            "o_status": o_status,
            "dispatched": dispatched,
            "to_be_evaluated": to_be_evaluated,
            "all_orders": all_orders
        }

if __name__ == '__main__':
    MineDao().mine_query()