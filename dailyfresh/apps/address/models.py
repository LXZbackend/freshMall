from django.db import models
from utils.models import BaseModel
from apps.passport.models import Passport


class Address(BaseModel):

    """
    购物车
    """

    user = models.ForeignKey(Passport, help_text='用户')

    recipient_name = models.CharField(blank=True,null=True,max_length=32,help_text='收件人姓名')

    recipient_phone = models.CharField(blank=True,null=True,max_length=11,help_text='收件人电话') 

    province = models.CharField(blank=True, null=True, max_length=32,
                                help_text='省')
    city = models.CharField(blank=True, null=True, max_length=32,
                            help_text='市')
    county = models.CharField(blank=True, null=True, max_length=32,
                              help_text='县')
    addr_detail = models.CharField(blank=True, null=True, max_length=64,
                                   help_text='详细地址')
    zip_code = models.CharField(blank=True, null=True, max_length=10, help_text='邮编')

    class Meta:
        db_table = 's_address'
