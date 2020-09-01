from django.db import models


class Type(models.Model):
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name


class Good(models.Model):
    good_name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.good_name


class StockOperate(models.Model):
    the_time = models.DateTimeField('Stock Operate time')
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    operate_quantity = models.IntegerField(default=0)
    note = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.operate_quantity) + ' ' + self.good.good_name
