from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Product, OrderItem, Order
# Register your models here.

#admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    pass
