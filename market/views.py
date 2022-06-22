import random

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Max
from django.http import HttpResponseForbidden, request
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from cart.forms import CartAddProductForm
from market.forms import ReviewCreateForm, UserCreateForm, FeedbackForm, AddToFavoritesForm
from market.models import Product, Reviews, Category, Stocks, Subcategory, CustomUser, Favorites
from parsing_currency import euro, dollar


class IndexView(ListView):
    model = Product
    template_name = "market/index.html"
    context_object_name = "products"

    def get_queryset(self):
        max_id = Product.objects.all().aggregate(max_pk=Max("pk"))['max_pk']
        for pk in range(1, max_id):
            pk = random.randint(1, max_id - 2)
            return Product.objects.filter(pk__gte=pk)


def login(request):
    if request.method == "GET":
        return redirect("accounts/login.html")


def logout(request):
    if request.method == "GET":
        return redirect("accounts/logged_out.html")


class RegisterUser(CreateView):
    form_class = UserCreateForm
    template_name = 'market/registration.html'
    success_url = reverse_lazy("registration_done")

    def form_valid(self, form):
        msg_html = render_to_string('market/register_done_mail.html')
        data = form.data
        subject = f'Сообщение от marketstuffdjango@gmail.com.Тема: Регистрация на сайте'
        content = "Регистрация прошла успешно!"
        form.save()
        new_user = User.objects.get(username=data["username"])
        create_city = CustomUser.objects.create(city=data["city"], user_for_city=new_user)
        create_city.save()
        send_mail(subject, content,
                  'DjangoMarket@yandex.by',
                  [data["email"]],
                  fail_silently=False,
                  html_message=msg_html
                  )
        return super().form_valid(form)


class Register_done(TemplateView):
    template_name = "market/registration_done.html"


class AboutMarketView(TemplateView):
    template_name = "market/about_market.html"


from django.db.models import Q


class ProductView(TemplateView):
    template_name = "market/product.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["product"] = Product.objects.get(pk=context["product_pk"])
        context["reviews"] = Reviews.objects.filter(product=context["product_pk"])
        product = Product.objects.get(pk=context["product_pk"])
        context["euro"] = round((product.price / float(euro)), 2)
        context["dollar"] = round((product.price / float(dollar)), 2)
        context["cart_product_form"] = CartAddProductForm()
        context["add_to_favorites_form"] = AddToFavoritesForm()
        if request.user.is_authenticated:
            favorites_products = list(
                Favorites.objects.filter(Q(user=request.user) & Q(product_favorite=context["product_pk"])))
            if len(favorites_products) > 0:
                context["favorites_products"] = "Товар в Избранном"
        return self.render_to_response(context)


class CatalogView(ListView):
    model = Category
    template_name = "market/catalog.html"
    context_object_name = "categories"
    queryset = Category.objects.all()


class СategoryView(ListView):
    model = Subcategory
    template_name = "market/category.html"
    context_object_name = "subcategories"

    def get_queryset(self):
        return Subcategory.objects.filter(category_id=self.kwargs['category_pk'])


class SubcategoryView(ListView):
    model = Subcategory
    template_name = "market/subcategory.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(subcategory_id=self.kwargs['subcategory_pk'])


class ProductCategoryView(TemplateView):
    template_name = "market/category.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=context["category_pk"])
        context["category"] = Category.objects.get(pk=context['category_pk'])
        return self.render_to_response(context)


class StocksView(ListView):
    model = Stocks
    template_name = "market/stocks.html"
    context_object_name = "stocks"
    queryset = Stocks.objects.all()


class StocksInfoView(TemplateView):
    template_name = "market/stock_info.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["stock"] = Stocks.objects.get(pk=context["stocks_pk"])
        return self.render_to_response(context)


class DeliveryView(TemplateView):
    template_name = "market/delivery.html"


class DiscountView(TemplateView):
    template_name = "market/discount.html"


class AddedReviewView(TemplateView):
    template_name = "market/added_review.html"


class AddReview(FormView):
    form_class = ReviewCreateForm
    success_url = reverse_lazy("added_review")
    template_name = "market/add_review.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        form.save()
        return super().form_valid(form)


class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'market/feedback.html'
    success_url = reverse_lazy("feedback_done")

    def form_valid(self, form):
        msg_html = render_to_string('market/feedback_mail.html')
        data = form.data
        subject = f'Сообщение от {data["email_sender"]}.Тема: {data["topic"]}'
        content = data["text_message"]
        form.save()
        send_mail(subject, content,
                  'DjangoMarket@yandex.by',
                  ['DjangoMarket@yandex.by'],
                  fail_silently=False,
                  html_message=msg_html
                  )
        return super().form_valid(form)


class FeedbackDone(TemplateView):
    template_name = "market/feedback_done.html"


class SearchResultsView(ListView):
    template_name = 'market/search_results.html'
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('search_line')
        object_list = Product.objects.filter(name__icontains=str(query))
        return object_list


class SearchView(TemplateView):
    template_name = "market/search.html"


def add_to_favorites(request, product_pk):
    user = request.user
    product = Product.objects.get(pk=product_pk)
    data = {'product_favorite': product.pk,
            'user': user.pk}
    form2 = AddToFavoritesForm(data=data)
    form2.save()
    return redirect('added_to_favorites')


class ProductAlreadyFavorites(TemplateView):
    template_name = "market/product_already_in_favorites.html"


def remove_from_favorites(request, product_favorite_pk):
    user_favorites = Favorites.objects.filter(user=request.user).get(product_favorite=product_favorite_pk)
    user_favorites.delete()
    return redirect("removed_favorite")


class RemovedFavorite(TemplateView):
    template_name = "market/removed_favorite.html"


class AddedToFavorites(TemplateView):
    template_name = 'market/added_to_favorites.html'


class FavoritesView(ListView):
    model = Favorites
    template_name = "market/favorites.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)
