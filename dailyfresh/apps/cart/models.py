from django.db import models
from utils.models import BaseModel
from apps.goods.models import Goods
from apps.passport.models import Passport

class Cart(BaseModel):

    """
    购物车
    """

    user = models.ForeignKey(Passport, help_text='用户')
    goods = models.ForeignKey(Goods, help_text='商品')
    goods_num = models.SmallIntegerField(default=1, help_text='商品数量')

    class Meta:
        db_table = 's_cart'

