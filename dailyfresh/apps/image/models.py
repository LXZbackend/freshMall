from django.db import models
from utils.models import BaseModel
from apps.goods.models import *


class Image(BaseModel):

    """
    图片存储
    """

    img_product_id = models.ForeignKey(Goods, help_text='商品ID')
    img_url = models.ImageField(
        upload_to='goods', blank=False, help_text='图片url路径')
    img_type = models.CharField(max_length=64, help_text='图片mime类型')
    img_is_def = models.BooleanField(default=False, help_text='是否默认')

    class Meta:
        db_table = 's_image'


