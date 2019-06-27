from django.db import models


class YGMain(models.Model):
    img = models.CharField(max_length=255,verbose_name='图片')
    name = models.CharField(max_length=50,verbose_name='图片名称')
    trackid = models.IntegerField(verbose_name='图片ID')

    class Meta:
        abstract = True  # 抽象类


class YGWheel(YGMain):

    class Meta:
        db_table = 'wheel'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class YGChosen(YGMain):

    class Meta:
        db_table = 'chosen'
        verbose_name = '精选推荐'
        verbose_name_plural = verbose_name


class YGNav(YGMain):

    class Meta:
        db_table = 'nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name


class YGNavDetail(YGMain):
    yg_productid = models.IntegerField()

    class Meta:
        db_table = 'details'
        verbose_name = '导航详情'
        verbose_name_plural = verbose_name


class YGGoods(models.Model):
    goodsid = models.IntegerField(verbose_name='商品编号')  # 商品id(商品编号)
    goods_wheel_img = models.CharField(max_length=255,verbose_name='商品图片')  # 轮播图  img[0] 对应的是 》小类id '40001:苹果'
    goodsname = models.CharField(max_length=50, verbose_name='商品名称')  # 商品名
    goods_desc = models.CharField(max_length=100, verbose_name='商品描述')  # 商品描述
#    ygg_pmdesc = models.BooleanField(default=False)
    price = models.FloatField(verbose_name='商品价格')   # 实际价格
    marketprice = models.FloatField(verbose_name='市场价格') # 市场价
    goods_groupid = models.CharField(max_length=20, verbose_name='一级类别编号')  # 大类id  '30001:进口水果'
    goods_childcid = models.CharField(max_length=20, verbose_name='二级类别编号')  # 小类id '40001:苹果'
    detail_img = models.CharField(max_length=1000, verbose_name='详情页图片')  # 详情页图片   'url#url#url'
    stock = models.IntegerField(verbose_name='库存')  # 库存
    sale = models.IntegerField(verbose_name='销量')  # 销量
    # ygg_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'goods'
        verbose_name = '商品表'
        verbose_name_plural = verbose_name


class YGUser(models.Model):
    phone = models.IntegerField(verbose_name='手机号码')
#    name = models.CharField(max_length=20, verbose_name='用户名')  # 用户名
    nickname = models.CharField(max_length=20, verbose_name='昵称')  # 昵称
    gender = models.BooleanField(default=True, verbose_name='性别')  # 默认男 True  女是False
    password = models.CharField(max_length=256, verbose_name='用户密码')
    idcard = models.CharField(max_length=20, verbose_name='身份证', null=True)  # 身份证
    img = models.CharField(max_length=30, verbose_name='用户图像')   # 用户图像
    balance = models.FloatField(verbose_name='账户余额')
    level = models.CharField(max_length=20, verbose_name='用户等级')

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class YGAddress(models.Model):
    user = models.ForeignKey(YGUser, on_delete=models.CASCADE,verbose_name='用户ID')
    address = models.CharField(max_length=500,verbose_name='用户地址')

    class Meta:
        db_table = 'address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name


class YGCart(models.Model):
    c_user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    c_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE, verbose_name='商品ID')
    c_goods_num = models.IntegerField(default=1,verbose_name='商品数量')
    c_is_select = models.BooleanField(default=True,verbose_name='是否选中')  # 是否选中，默认为选中

    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


# ORDER_STATUS
# # 已下单未付款
# ORDER_STATUS_NOT_PAY = 0
# # 已下单已付款未发货
# ORDER_STATUS_NOT_SEND = 1
# # 已下单已付款已发货未收货
# ORDER_STATUS_NOT_RECEIVE = 2
# # 已下单已付款已发货已收货未确认
# ORDER_STATUS_NOT_AFFIRM = 3
# # 已下单已付款已发货已收货已确认未评价
# ORDER_STATUS_NOT_EVALUATE = 4
# # 已下单已付款已发货已收货已确认已评价未追评
# ORDER_STATUS_NOT_REVIEW = 5
# # 已下单已付款已发货已收货已确认已评价
# ORDER_STATUS_ORDER_STATUS_COMPLETE= 6


class YGOrder(models.Model):
    ORDER_STATUS = ((0, '已下单未付款'),
                    (1, '已下单已付款待收货'),
                    (2, '下单后待评论'))
    # (3,'已下单已付款已发货已收货未确认'),
    # (4,'已下单已付款已发货已收货已确认未评价'),
    # (5,'已下单已付款已发货已收货已确认已评价未追评'),
    # (6,'已下单已付款已发货已收货已确认已评价'),)
    o_user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    o_price = models.FloatField(verbose_name='总价格')
    o_time = models.DateTimeField(auto_now=True, verbose_name='下单时间')
    o_status = models.IntegerField(default=ORDER_STATUS[0], verbose_name='订单状态')

    class Meta:
        db_table = 'ygoders'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class YGOderDetail(models.Model):
    o_order = models.ForeignKey(YGOrder, on_delete=models.CASCADE,verbose_name='订单ID')
    o_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE,verbose_name='商品ID')
    o_goods_num = models.IntegerField(default=1,verbose_name='商品数量')

    class Meta:
        db_table = 'ygoderdetail'
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class YGComment(models.Model):
    user = models.ForeignKey(YGUser, on_delete=models.CASCADE, verbose_name='用户ID')
    order_id = models.ForeignKey(YGOrder, on_delete=models.CASCADE, verbose_name='订单ID')
    comments = models.CharField(max_length=500,verbose_name='用户评论')

    class Meta:
        db_table = 'comments'
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name


class YGEat(models.Model):
    eat_img = models.CharField(max_length=256, verbose_name='图片')
    eat_content = models.CharField(max_length=200, verbose_name='描述')
    eat_time = models.CharField(max_length=50, verbose_name='时间')

    class Meta:
        db_table = 'ygeat'
        verbose_name = '吃喝玩乐'
        verbose_name_plural = verbose_name





