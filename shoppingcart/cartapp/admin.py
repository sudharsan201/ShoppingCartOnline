from django.contrib import admin

# Register your models here.
from cartapp.models import Product, Order, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
