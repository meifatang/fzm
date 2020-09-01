from django.contrib import admin
from .models import Type, Good, StockOperate

# Register your models here.

admin.site.register(Type)
admin.site.register(Good)
admin.site.register(StockOperate)
