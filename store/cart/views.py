from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from coupons.forms import CouponForm
from market.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_pk)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})
    coupon_apply_form = CouponForm()
    return render(request, 'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})
