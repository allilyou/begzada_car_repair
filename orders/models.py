from django.db import models

# Create your models here.
from main.models import AutoPart


class Order(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    service = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    comment = models.TextField(max_length=250)

    need_moderation = models.BooleanField(default=True)

    def __str__(self):
        return f"Заказ #{self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'


class OrderAutoPart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    auto_part = models.ForeignKey(AutoPart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '-'
