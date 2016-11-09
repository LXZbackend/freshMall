from django.db import models
from utils.models import BaseModel
from apps.passport.models import Passport
from apps.address.models import Address
from apps.goods.models import Goods


class SOrder(BaseModel):

    """
    订单
    """

    PAYING = 1
    PAYED = 2
    CANCELED = 3
    DELETED = 4

    user = models.ForeignKey(Passport, help_text='用户')
    addr = models.ForeignKey(Address, help_text="地址")
    total_amount = models.FloatField(default=0.0, help_text='订单总额')
    total_count  = models.SmallIntegerField(default=1, help_text='订单商品数量')
    ex_price = models.FloatField(default=10.0, help_text='商品运费')
    # 1:支付宝  2:微信  3:银行卡  4:货到付款
    payment_method = models.SmallIntegerField(default=1, help_text='支付方式')
    # 1:待支付  2:已支付  4:已删除
    order_status = models.SmallIntegerField(default=1, help_text='订单状态')

    class Meta:
        db_table = 's_order'


class SOrderGoods(BaseModel):
    """
    订单商品
    """

    sorder = models.ForeignKey(SOrder, help_text='订单')
    goods = models.ForeignKey(Goods, help_text='商品')
    goods_price = models.FloatField(default=0.0, help_text='商品单价')
    goods_count = models.SmallIntegerField(default=1, help_text='商品数量')
    comment = models.TextField(default='', help_text='商品评价')

    class Meta:
        db_table = 's_order_goods'