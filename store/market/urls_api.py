from django.urls import path
from market.views_api import ProductViewSet, AddReviewViewSet, CategoryViewSet

urlpatterns = [
    path('category/', CategoryViewSet.as_view({"get": "list"})),
    path('category/<int:pk>/', CategoryViewSet.as_view({"get": "retrieve"})),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': "retrieve"})),
    path('product/<int:pk>/add_review/', AddReviewViewSet.as_view({"get": "retrieve", "post":"create"})),
    path('product/', ProductViewSet.as_view({'get': "list"})),

]
