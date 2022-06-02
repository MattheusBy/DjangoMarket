from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            send_mail("Вы успешно оформили заказ!", "Ваш заказ будет доставлен в ближайшее время",
                      'marketstuffdjango@gmail.com',
                      [form.instance.email],
                      fail_silently=False, )

            request.session['order_id'] = order.id
            return redirect(reverse('process'))
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})