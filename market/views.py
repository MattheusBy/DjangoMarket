import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Max
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from cart.forms import CartAddProductForm
from coupons.models import Coupon
from market.forms import ReviewCreateForm, UserCreateForm, FeedbackForm, AddToFavoritesForm
from market.models import Product, Reviews, Category, Stocks, Subcategory, CustomUser, Favorites
from parsing_currency import euro, dollar
from django.db.models import Q

class IndexView(ListView):
    """ Displays start page. It shows three random products from catalog"""
    model = Product
    template_name = "market/index.html"
    context_object_name = "products"

    def get_queryset(self):
        max_id = Product.objects.all().aggregate(max_pk=Max("pk"))['max_pk']
        for pk in range(1, max_id):
            pk = random.randint(1, max_id - 2)
            return Product.objects.filter(pk__gte=pk)


def login(request):
    """ Function for login """
    if request.method == "GET":
        return redirect("accounts/login.html")


def logout(request):
    """ Function for logout """
    if request.method == "GET":
        return redirect("accounts/logged_out.html")


class RegisterUser(CreateView):
    """ Class for register. Shows RegisterForm and create new user 
    for app.After successful register sends letter to email """
    form_class = UserCreateForm
    template_name = 'market/registration.html'
    success_url = reverse_lazy("registration_done")

    def form_valid(self, form):
        msg_html = render_to_string('market/register_done_mail.html')
        data = form.data
        subject = f'Сообщение от DjangoMarket@yandex.by.Тема: Регистрация на сайте'
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
    """ View template after successful register"""
    template_name = "market/registration_done.html"


class AboutMarketView(TemplateView):
    """ View template with description about shop"""
    template_name = "market/about_market.html"


class ProductView(TemplateView):
    """ View all information about each product: price,image,description,reviews. 
    Provides to add product in cart, favorites"""
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
    """ Views all categories of products"""
    model = Category
    template_name = "market/catalog.html"
    context_object_name = "categories"
    queryset = Category.objects.all()


class СategoryView(ListView):
    """ Views all subcategories of products for each category"""
    model = Subcategory
    template_name = "market/category.html"
    context_object_name = "subcategories"

    def get_queryset(self):
        return Subcategory.objects.filter(category_id=self.kwargs['category_pk'])


class SubcategoryView(ListView):
    """ Shows all subcategories for each category"""
    model = Subcategory
    template_name = "market/subcategory.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(subcategory_id=self.kwargs['subcategory_pk'])


class ProductCategoryView(TemplateView):
    """ Shows all products for each subcategory """
    template_name = "market/category.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=context["category_pk"])
        context["category"] = Category.objects.get(pk=context['category_pk'])
        return self.render_to_response(context)


class StocksView(ListView):
    """ Displays all current stocks """
    model = Coupon
    template_name = "market/stocks.html"
    context_object_name = "coupon"
    queryset = Coupon.objects.all()


class StocksInfoView(TemplateView):
    """ Provides information for stock """
    template_name = "market/stock_info.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["coupon"] = Coupon.objects.get(pk=context["coupon_pk"])
        return self.render_to_response(context)


class DeliveryView(TemplateView):
    """ Shows delivery terms """
    template_name = "market/delivery.html"


class DiscountView(TemplateView):
    """ Views information about disconts """
    template_name = "market/discount.html"


class AddedReviewView(TemplateView):
    """ Shows template after successful add review """
    template_name = "market/added_review.html"


class AddReview(FormView):
    """ Provides possibility for add review """
    form_class = ReviewCreateForm
    success_url = reverse_lazy("added_review")
    template_name = "market/add_review.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        form.save()
        return super().form_valid(form)


class FeedbackView(CreateView):
    """ Class provides possibility to send user's quetions. Requires user's email-address, topic.
    After input correct data sends letter to staff email"""
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
    """ Shows template after successful add review"""
    template_name = "market/feedback_done.html"


class SearchResultsView(ListView):
    """ Displays results of search. Shows all products which contains search words"""
    template_name = 'market/search_results.html'
    model = Product

    def get_queryset(self):
        query = self.request.GET.get('search_line')
        object_list = Product.objects.filter(name__icontains=str(query))
        return object_list


class SearchView(TemplateView):
    """ Shows page with search form """
    template_name = "market/search.html"


def add_to_favorites(request, product_pk):
    """ Function for add current product to favorites """
    user = request.user
    product = Product.objects.get(pk=product_pk)
    data = {'product_favorite': product.pk,
            'user': user.pk}
    form2 = AddToFavoritesForm(data=data)
    form2.save()
    return redirect('added_to_favorites')


class ProductAlreadyFavorites(TemplateView):
    """ Shows page with information if current product already in user's favorites """
    template_name = "market/product_already_in_favorites.html"


def remove_from_favorites(request, product_favorite_pk):
    """ Provides to delete current product from favorites """
    user_favorites = Favorites.objects.filter(user=request.user).get(product_favorite=product_favorite_pk)
    user_favorites.delete()
    return redirect("removed_favorite")


class RemovedFavorite(TemplateView):
    """ Template for successful remove from user's favorites """
    template_name = "market/removed_favorite.html"


class AddedToFavorites(TemplateView):
    """ Show information after successful add to favorites """
    template_name = 'market/added_to_favorites.html'


class FavoritesView(ListView):
    """ Shows list with all favorite products for current user """
    model = Favorites
    template_name = "market/favorites.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return Favorites.objects.filter(user=self.request.user)
