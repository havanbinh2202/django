from django.contrib import admin
from .models import Product, Category, CartItem,ShippingAddress

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
