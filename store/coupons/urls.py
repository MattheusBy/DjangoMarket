from django.urls import path
from .views import coupon_apply

urlpatterns = [
    path('coupons/', coupon_apply, name='apply_coupon'),
]
