from django.db import models
from utils.models import BaseModel
from jsonfield import JSONField


class Goods(BaseModel):

    """
    商品表
    """
    YES = 1
    NO = 2
    
    ONLINE = 1
    OFFLINE = 2
    DELETED = 3

    goods_type_id = models.SmallIntegerField(default=1, help_text='商品分类ID')
    goods_name = models.CharField(default="", max_length=64, help_text='商品名称')
    goods_subtitle = models.CharField(default="", max_length=128, help_text='商品副标题')
    goods_price = models.FloatField(default=0.0, help_text='商品价格')
    goods_unit = models.IntegerField(default=1,help_text='商品单位')
    goods_ex_price = models.FloatField(default=0.0, help_text='商品运费')
    goods_info = models.TextField(help_text='商品描述')
    goods_status = models.IntegerField(default=ONLINE, help_text='商品状态')
    goods_stock = models.IntegerField(default=1,help_text='商品库存')
    goods_sales = models.IntegerField(default=1,help_text='商品销量')

    class Meta:
        db_table = 's_goods'

    def __str__(self):
        return '%s %s' % (self.id, self.goods_name)

    @classmethod
    def get_one_goods(cls, goods_id):
        return cls.objects.get(id=goods_id)

    @classmethod
    def get_goods_by_type(cls, goods_type_id, limit=None, sort='default'):
        if 'price' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('goods_price')
        elif 'hot' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('-goods_sales')
        elif 'new' == sort:
            data = cls.objects.filter(goods_type_id=goods_type_id).order_by('-create_time')
        else:
            data = cls.objects.filter(goods_type_id=goods_type_id)
        if None == limit:
            return data
        else:
            return data[:limit]

