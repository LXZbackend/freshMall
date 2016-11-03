# coding=utf-8

from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


class ShopCartManager(models.Manager):
    def get_queryset(self):
        return super(ShopCartManager, self).get_queryset().filter(isDelete=False)


class UserInfo(models.Model):
	'''
		用户个人信息表
	'''
	account = models.CharField(max_length=20)
	passswd = models.CharField(max_length=20)
	# name = models.CharField(max_length=20,defaultkj udvb k)
	# telephone = models.CharField(max_length=11)
	email= models.CharField(max_length=30)
	isDelete = models.BooleanField(default = False)

	def __str__(self):
		return self.account.encode('utf-8')



class Consignee(models.Model):
	'''
		收件人地址信息表
	'''
	# 收货人姓名
	recePerName = models.CharField(max_length=20)
	# 收货人电话
	recePerTel = models.CharField(max_length=11)
	# 收货人地址
	addr = models.CharField(max_length=1000)
	# 邮编
	postCode = models.IntegerField(default=0)
	# 设置逻辑删除
	isDelete = models.BooleanField(default=False)
	# 设置外键，确认每条信息是那个用户的表 用户的主键编号
	userNum = models.ForeignKey('UserInfo')
	

# 商品类表
class GoodsClass(models.Model):
	#id自增
	className = models.CharField(max_length=20)#类名

	def __str__(self):
		return self.className.encode('utf-8')

# 商品表
class GoodsList(models.Model):
	#id自增
	goodsName = models.CharField(max_length=50)#商品名
	goodsResume=models.CharField(max_length=80)	#商品摘要
	goodsDetail=HTMLField()#商品详情描述
	goodsRoute = models.ImageField(upload_to='uploads/')#商品图片路径
	goodsStock = models.CharField(max_length=50)#商品库存信息
	goodsPrice = models.DecimalField(max_digits=6,decimal_places=2)#商品价格
	goodsType = models.ForeignKey('GoodsClass')#商品父类
	buyTimes = models.IntegerField() #商品购买次数（人气）
	goodsUnit = models.CharField(max_length=20)	# 商品规格
	goodsPubdate = models.DateTimeField()	#商品发布时间
	
	def __str__(self):
		return self.goodsName.encode('utf-8')



# 购物车
class ShoppingCart(models.Model):

	goodsId = models.ForeignKey('GoodsList')#商品id

	userId = models.ForeignKey('UserInfo')#用户id

	c = models.IntegerField()#数量

	total = models.FloatField()#小计

	isDelete = models.BooleanField(default=False)	#是否删除
	# 重写管理方法
	# objects = ShopCartManager()







# 订单表
class OrderForm(models.Model):
	#订单时间
	orderDate = models.DateTimeField()
	#用户id外键指向用户表的主键
	userId = models.ForeignKey('UserInfo')
	#订单编号 自己写规则生成
	orderNum= models.IntegerField()


class OrderDetail(models.Model):
	'''订单详情表
	'''
	# 外键商品id
	goodsId = models.ForeignKey('GoodsList')
	# 订单idX
	orderId = models.ForeignKey('OrderForm')
	
	# 数量
	goodsCount =models.IntegerField()
	# 总金额
	orderSum = models.DecimalField(max_digits=6, decimal_places=2)
	# 用户id
	# userId = models.ForeignKey('UserInfo')
	#是否付款 (订单状态)
	isPay = models.BooleanField()
	def orderStatus(self):
		if self.isPay:
			return "已付款"
		else:
			return "未付款"
		orderStatus.short_description = "订单状态"
