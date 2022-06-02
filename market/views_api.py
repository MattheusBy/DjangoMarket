from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from market.models import Product, Category, Reviews
from market.serializers import ProductSerializer, CategorySerializer, AddReviewSerializer, OrderSerializer
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class APICategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class APICategoryDetail(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.all()[:2]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AddReviewViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = Reviews

    def retrieve(self, request, *args, **kwargs):
        product = Product.objects.get(pk=kwargs['pk'])
        serializer = ProductSerializer
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AddReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class APIOrder(RetrieveModelMixin, CreateModelMixin, APIView):
    def retrieve(self, request, *args, **kwargs):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
