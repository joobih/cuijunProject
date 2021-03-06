#encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
import datetime

#会员表
class User(models.Model):
    name = models.CharField(max_length = 20, verbose_name = "会员姓名")			#会员姓名
    phone = models.CharField(max_length = 30, verbose_name = "会员电话")        #会员电话
    email = models.CharField(max_length = 30, verbose_name = "会员邮箱")        #会员邮箱
    password = models.CharField(max_length = 50, verbose_name = "密码")         #登录密码
    create_at = models.DateTimeField(default = datetime.datetime.now(), verbose_name = "创建时间")
    
    class Meta:
        verbose_name = u"会员用户"
        verbose_name_plural = u"会员用户"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name.encode('utf-8')

#def get_default_user():
#    return User.objects.get(id=1)
#留言表
class LeaveMessage(models.Model):
    user = models.ForeignKey(User, related_name="usermessages", verbose_name = "会员名")
    title = models.CharField(max_length = 50,verbose_name = "标题")
    content = models.CharField(max_length = 255, verbose_name = "留言内容")
    create_time = models.DateTimeField(default = datetime.datetime.now(), verbose_name = "留言时间")

    class Meta:
        verbose_name = u"留言表"
        verbose_name_plural = u"留言表"
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title.encode('utf-8')

    def get_queryset(self):
        return super(LeaveMessage, self).get_queryset().order_by('-create_time')

class BoutiqueLine(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "精品路线名称")           #精品路线的名字
    days = models.IntegerField()                                                       #需要的天数
    pic_address = models.CharField(max_length = 255, verbose_name = "图片地址")        #默认图片的地址
    map_pic_address = models.CharField(max_length = 255, null = True, verbose_name = "地图地址")      #路线总览地图地址
    price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)      #参考价格
    
    class Meta:
        verbose_name = u"精品路线"
        verbose_name_plural = u"精品路线"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name.encode('utf-8')

#def get_default_boutiqueline():
#    return BoutiqueLine.objects.get(id=1)

class BoutiqueLineDetails(models.Model):
    boutiqueline = models.ForeignKey(BoutiqueLine, related_name="boutiqueline", verbose_name = "精品路线")
    day_numbers = models.IntegerField(verbose_name = "第几天")                                        #由精品路线中的days字段决定的第几天的天数。
    node_details = models.TextField(null = True, verbose_name ="路途描述")
    approach = models.CharField(max_length = 255, null = True, verbose_name = "途径地描述")           #途径地的描述
    detail_pic_number = models.IntegerField(null = True, verbose_name = "小图的数目")                 #描述小图的数目
    detail_pic_address = models.TextField(null = True, verbose_name = "每张图的地址")                 #描述小图的图片地址

    class Meta:
        verbose_name = u"精品路线详情"
        verbose_name_plural = u"精品路线详情"

    def __unicode__(self):
        return self.boutiqueline.name + "--" + self.approach

    def __str__(self):
        return (self.boutiqueline.name + "--" + self.approach).encode('utf-8')
#    def __unicode(self):
      

class PrivateOrder(models.Model):
    ACTIVE_STATUS = 0
    FINISHED_STATUS = 1
    CANCLE_STATUS = -1
    status_t = ((ACTIVE_STATUS,"未完成"),(FINISHED_STATUS,"已完成"),(CANCLE_STATUS,"取消订单"))
    name = models.CharField(max_length = 20, verbose_name = "用户姓名")                                    #私人订制提交姓名
    phone = models.CharField(max_length = 30, verbose_name = "用户电话")                                   #私人订制提交电话
    status = models.IntegerField(default = 0, verbose_name = "完成状态", choices = status_t)               #私人订制方案完成状态：0--未完成；1--已完成；-1--用户取消
    destination = models.CharField(max_length = 255, verbose_name = "目的地")                              #私人订制目的地
    days = models.PositiveIntegerField(null = True, verbose_name = "预计游玩天数")                         #私人订制预计游玩天数
    price = models.DecimalField(max_digits = 10, decimal_places = 3,null = True, verbose_name = "预计价格")      #私人订制客户预计价格
    approach = models.CharField(max_length = 255, null = True, verbose_name = "预留途径地")                      #用户预留途径地
    hotel = models.CharField(max_length = 60, null = True, verbose_name = "住宿要求")                                #住宿
    travel_requirement = models.CharField(max_length = 255, null = True, verbose_name = "出行要求")
    
    class Meta:
        verbose_name = u"私人订制"
        verbose_name_plural = u"私人订制"
    def __str__(self):
        return (u"私人订制--" + self.name).encode("utf-8")



admin.site.register(BoutiqueLine)
admin.site.register(BoutiqueLineDetails)
admin.site.register(PrivateOrder)
admin.site.register(User)
admin.site.register(LeaveMessage)
# Create your models here.
