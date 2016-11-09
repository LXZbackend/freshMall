import json
from .models import Goods
from .enums import *


class GoodsLogic(object):

    """
    商品逻辑
    """

    @classmethod
    def get_one_goods(cls, goods_id):
        data = Goods.get_one_goods(goods_id)
        data.price = "%.2f" % data.goods_price
        data.img = data.image_set.all()[0].img_url
        data.type_name = GOODS_TYPE[data.goods_type_id]
        return data


    @classmethod
    def get_goods_by_type(cls, goods_type_id, limit=None, sort='default'):
        data = Goods.get_goods_by_type(goods_type_id, limit, sort)
        for i in data:
            i.price = "%.2f" % i.goods_price
            i.img = i.image_set.all()[0].img_url
        return data


