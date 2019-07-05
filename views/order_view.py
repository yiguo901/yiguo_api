# -*- coding: utf-8 -*-
# @Time : 2019/7/2 10:08

from flask import Blueprint
from flask import request, jsonify

from dao.order_dao import Order_Dao

from libs import cache

blue_order = Blueprint('order_api', __name__)


@blue_order.route('/order/', methods=('POST',))
def user_add_order():
    from views import check_requirments
    check_errors = check_requirments("POST",
                                     'token', 'addr_id',
                                     'goods_ids', 'goods_cnt')
    if check_errors:
        return jsonify({
            'code': 202,
            'msg': check_errors
        })

    user_id = cache.get_token_user_id(request.form.get('token'))
    orderDao = Order_Dao()
    # orders
    goods_ids = request.form.get('goods_ids')
    goods_cnt = request.form.get('goods_cnt')
    addr_id = request.form.get('addr_id')
    goods = [orderDao.goods_by_id(goods_id) for goods_id in goods_ids.split(',')]
    total_price = sum([ goods[index]['price'] * int(cnt) for index, cnt in enumerate(goods_cnt.split(','))])
    order_id = orderDao.get_order_id()
    # order_detail
    # select last_insert_id()

    data = {
        'order_id':order_id,
        'o_user':user_id,
        'o_price':total_price,
        'o_status':0,
        'addr_id':addr_id
    }
    orderDao.save(**data)
    return jsonify({
        'code': 200,
        'total_price': total_price,
        'goods': goods,
        'addr_id':addr_id,
        'order_id':order_id
    })
@blue_order.route('/order/pay/', methods=('POST',))
def pay_order():
    from views import check_requirments
    check_errors = check_requirments("POST",
                                     'token', 'addr_id',
                                     'goods_ids', 'goods_cnt','o_status')
    if check_errors:
        return jsonify({
            'code': 202,
            'msg': check_errors
        })
    user_id = cache.get_token_user_id(request.form.get('token'))
    o_status = request.form.get('o_status')
    if o_status == '0':
        #跳转到支付页面
        orderDao = Order_Dao()
        balance = orderDao.query_user_sale(user_id)
        total_price = request.form.get('total_price')
        order_id = request.form.get('order_id')
        if balance >= total_price:
            balance -= total_price
            #更新用户余额
            orderDao.to_update_order('1',user_id,order_id)
        # rd.set(order_id, 250)
        # rd.expire(order_id, 24 * 3600)
        #
        # if not rd.get(order_id):
        #     orderDao.to_update_order('2', user_id, order_id)
            return jsonify({
                'code': 200,
                'msg': '支付成功！'
            })
        else:
            return jsonify({
                'code': 201,
                'msg': '余额不足！'
            })






