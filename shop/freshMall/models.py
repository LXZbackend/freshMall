#coding=utf-8
from django.db import models

# Create your models here.
class userInfo(models.Model):
	'''
		用户个人信息的表
	'''
	account = models.CharField(max_length=20)
	passswd = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	telephone = models.CharField(max_length=11)
	email= models.CharField(max_length=30)
	isDelete = models.BooleanField(default = False)

	def __str__(self):
		return self.account.encode('utf-8')
class consignee(models.Model):
	'''
		收件人的表
	'''
	# 收货人姓名
	recePerName = models.CharField(max_length=20)
	# 收货人电话
	recrPerTel = models.CharField(max_length=11)
	# 收货人地址
	addr = models.CharField(max_length=1000)
	# 邮编
	postcode = models.IntegerField(default=0)
	# 设置逻辑删除
	isDelete = models.BooleanField(default=False)
	# 设置外键，确认每条信息是那个用户的表 用户的主键编号
	userNum = models.ForeignKey('userInfo')
	


class goodsClass(models.Model):
	#id自增
	className = models.CharField(max_length=20)#类名
	def __str__(self):
		return self.className.encode('utf-8')


class goodsList(models.Model):
	#id自增
	goodsName = models.CharField(max_length=50)#商品名
	goodsDetail=models.CharField(max_length=1000)#商品详情描述
	goodsRoute = models.CharField(max_length=50)#商品图片路径
	goodsStock = models.CharField(max_length=50)#商品库存
	goodsPrice = models.DecimalField(max_digits=6,decimal_places=2)#商品价格
	goodsType = models.ForeignKey('goodsClass')#商品父类

	def __str__(self):
		return self.goodsName.encode('utf-8')

# 购物车
class shoppingCart(models.Model):

    goodsId = models.ForeignKey('goodsList')#商品id

    userInfo = models.ForeignKey('userInfo')#用户id

    amount = models.IntegerField()#数量

    total = models.FloatField()#小计



# 订单表
class orderForm(models.Model):
    #订单时间
	orderDate = models.DateTimeField()
	#用户id外键指向用户表的主键
	userId = models.ForeignKey('userInfo')

	def __str__(self):
		return self.id.encode('utf-8')

# 订单详情表：
# 商品id	goodsId
# 商品价格	goodsPrice
# 商品数量	goodsCount
# 订单金额：	orderSum
# 订单编号:	orderId

'''订单详情表
'''
class orderDetail(models.Model):
	# 外键商品id
	goodsId = models.ForeignKey('goodsList')
	orderId = models.ForeignKey('orderForm')

	#订单编号 自己写规则生成
	orderId = models.IntegerField()
	# 数量
	goodsCount =models.IntegerField()
	# 总金额
	orderSum = models.DecimalField(max_digits=6, decimal_places=2)
	#是否付款 订单状态
	isPay = models.BooleanField()
	def orderStatus(self):
		if self.isPay:
			return "已付款"
		else:
			return "待付款"
		orderStatus.short_description = "订单状态"

