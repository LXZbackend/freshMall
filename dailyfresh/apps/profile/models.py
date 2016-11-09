from django.db import models
from utils.models import BaseModel
from apps.passport.models import Passport
from apps.goods.models import Goods


class Profile(BaseModel):

    """
    用户信息表
    """

    user_id = models.IntegerField(help_text='用户ID')
    user_type = models.SmallIntegerField(default=1, help_text='用户类型')
    sex = models.IntegerField(help_text='性别', default=3)
    realname = models.CharField(blank=True, null=True, max_length=32,
                                help_text='真实姓名')
    province = models.CharField(blank=True, null=True, max_length=32,
                                help_text='省')
    city = models.CharField(blank=True, null=True, max_length=32,
                            help_text='市')
    county = models.CharField(blank=True, null=True, max_length=32,
                              help_text='县')
    addr_detail = models.CharField(blank=True, null=True, max_length=64,
                                   help_text='详细地址')

    class Meta:
        db_table = 's_user_profile'


class BrowseHistory(BaseModel):
    """
    用户浏览商品记录
    """
    user = models.ForeignKey(Passport, help_text='用户')
    goods = models.ForeignKey(Goods, help_text='商品')

    class Meta:
        db_table = 's_user_browse_history'