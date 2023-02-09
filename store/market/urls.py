"""
The collection of url-paths for market-application

"""

from django.urls import path
from market.views import ProductView, CatalogView, \
    StocksView, StocksInfoView, AboutMarketView, \
    login, logout, RegisterUser, AddedReviewView, \
    AddReview, Register_done, FeedbackView, FeedbackDone,\
    СategoryView, SubcategoryView, DeliveryView,\
    DiscountView, IndexView, SearchView, SearchResultsView,\
    AddedToFavorites, add_to_favorites, FavoritesView, \
    RemovedFavorite, remove_from_favorites

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('registration_done/', Register_done.as_view(),
         name="registration_done"),
    path('about_market/', AboutMarketView.as_view(),
         name="about_market"),
    path('product/<int:product_pk>/', ProductView.as_view(),
         name="product"),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('category/<int:category_pk>/', СategoryView.as_view(),
         name='show_category'),
    path('subcategory/<int:subcategory_pk>/', SubcategoryView.as_view(),
         name='show_subcategory'),
    path('add_review/<int:product_pk>/', AddReview.as_view(),
         name="add_review"),
    path('added_review/', AddedReviewView.as_view(),
         name="added_review"),
    path('product_list/', ProductView.as_view()),
    path('stocks/', StocksView.as_view(), name="stocks"),
    path('stocks_info/<int:stock_pk>/', StocksInfoView.as_view(),
         name="stocks_info"),
    path('delivery/', DeliveryView.as_view(), name="delivery"),
    path('discount/', DiscountView.as_view(), name="discount"),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path('feedback_done/', FeedbackDone.as_view(),
         name="feedback_done"),
    path('search/', SearchView.as_view(), name="search"),
    path('search_results/', SearchResultsView.as_view(),
         name="search_results"),
    path('added_to_favorites/', AddedToFavorites.as_view(),
         name="added_to_favorites"),
    path('add_to_favorites/<int:product_pk>/', add_to_favorites,
         name="add_to_favorites"),
    path('favorites/', FavoritesView.as_view(), name="favorites"),
    path('remove_favorite/<int:product_favorite_pk>/', remove_from_favorites,
         name="remove_favorite"),
    path('removed_favorite/', RemovedFavorite.as_view(),
         name="removed_favorite"),
]
