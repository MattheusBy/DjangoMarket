from django.contrib import admin
from market.models import Product, Reviews, Category, Stocks, Basket, Feedback, CustomUser, Subcategory

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Stocks)
admin.site.register(Basket)
admin.site.register(Feedback)
admin.site.register(CustomUser)
