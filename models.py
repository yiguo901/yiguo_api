from django.db import models


class YGMain(models.Model):
    img = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    trackid = models.IntegerField()

    class Meta:
        abstract = True


class YGWheel(YGMain):

    class Meta:
        db_table = 'ygwheel'


class YGChosen(YGMain):

    class Meta:
        db_table = 'ygchosen'


class YGNav(YGMain):

    class Meta:
        db_table = 'ygnav'


class YGNavDetail(YGMain):
    yg_productid = models.IntegerField()

    class Meta:
        db_table = 'ygnavdetails'


class YGGoods(models.Model):
    ygg_goodsid = models.IntegerField()  #商品id(商品编号)
    ygg_goods_wheel_img = models.CharField(max_length=255) #轮播图  img[0] 对应的是 》小类id '40001:苹果'
    ygg_goodsname = models.CharField(max_length=50)  #商品名
    ygg_goods_desc = models.CharField(max_length=100)  #商品描述
    # ygg_pmdesc = models.BooleanField(default=False)
    ygg_price = models.FloatField()   #实际价格
    ygg_marketprice = models.FloatField() #市场价
    ygg_goods_groupid = models.CharField(max_length=20) #大类id  '30001:进口水果'
    ygg_goods_childcid = models.CharField(max_length=20)  #小类id '40001:苹果'
    ygg_detail_img = models.CharField(max_length=1000)  # 详情页图片   'url#url#url'
    ygg_stock = models.IntegerField()  # 库存
    ygg_sale = models.IntegerField()  # 销量
    # ygg_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'yggoods'


class YGUser(models.Model):
    user_id = models.IntegerField(max_length=10, unique=True)
    user_pay_code = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=256)
    user_phone = models.IntegerField(max_length=20)
    user_gender = models.BooleanField()  # 默认男 True  女是False
    user_name = models.CharField(max_length=20) # 用户名
    user_idcard = models.CharField(max_length=20) #身份证
    user_img = models.CharField(max_length=30)  #用户图像
    user_nickname = models.CharField(max_length=20) #昵称
    

    class Meta:
        db_table = 'ygusers'

class YGAddress(models.Model):
    yg_user = models.ForeignKey(YGUser, on_delete=models.CASCADE)
    yg_addr = models.CharField(max_length=500)

    class Meta:
        db_table = 'ygaddress'

class YGComment(models.Model):
    yg_order = models.ForeignKey(YGUser, on_delete=models.CASCADE)
    yg_comments = models.CharField(max_length=500)


class YGCart(models.Model):
    c_user = models.ForeignKey(YGUser, on_delete=models.CASCADE)
    c_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE)
    c_goods_num = models.IntegerField(default=1)
    c_is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'ygcart'



# ORDER_STATUS
# 已下单未付款

ORDER_STATUS_NOT_PAY = 0
# 已下单已付款未发货
ORDER_STATUS_NOT_SEND = 1
# 已下单已付款已发货未收货
ORDER_STATUS_NOT_RECEIVE = 2
# 已下单已付款已发货已收货未确认
ORDER_STATUS_NOT_AFFIRM = 3
# 已下单已付款已发货已收货已确认未评价
ORDER_STATUS_NOT_EVALUATE = 4
# 已下单已付款已发货已收货已确认已评价未追评
ORDER_STATUS_NOT_REVIEW = 5
# 已下单已付款已发货已收货已确认已评价
ORDER_STATUS_ORDER_STATUS_COMPLETE= 6


class YGOder(models.Model):
    o_user = models.ForeignKey(YGUser,on_delete=models.CASCADE)
    o_price = models.FloatField()
    o_time = models.DateTimeField(auto_now=True)
    o_status = models.IntegerField(default=ORDER_STATUS_NOT_PAY)

    class Meta:
        db_table = 'ygoders'


class YGOderDetail(models.Model):
    o_order = models.ForeignKey(YGOder, on_delete=models.CASCADE)
    o_goods = models.ForeignKey(YGGoods, on_delete=models.CASCADE)
    o_goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'ygoderdetail'











