from django.contrib import admin
from django.urls import path, include
from market.views import CatalogView, IndexView
from django.conf.urls.static import static
from shop_server import settings

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('catalog/', CatalogView.as_view()),
    path('payment/', include('payment.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('coupons/', include('coupons.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('market/', include('market.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
