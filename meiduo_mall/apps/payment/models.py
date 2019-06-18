from django.db import models

from meiduo_mall.utils.models import BaseModel


# 定义支付结果模型类
class Payment(BaseModel):
    """支付信息"""
    order = models.ForeignKey("orders.OrderInfo", on_delete=models.CASCADE, verbose_name='订单')
    trade_id = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="支付编号")

    class Meta:
        db_table = 'tb_payment'
        verbose_name = '支付信息'
        verbose_name_plural = verbose_name
