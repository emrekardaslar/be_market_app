from django.contrib import admin
from .models import Product, Comment, Order, OrderItem, Rating, User, Category, Subcategory, Brand
# Register your models here.

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)