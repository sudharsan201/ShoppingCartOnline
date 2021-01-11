from django.shortcuts import render

# Create your views here.
from django_filters import OrderingFilter
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from cartapp.models import Product, Order, OrderItem
from cartapp.serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.UserId == request.user


class ProductList(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['id', 'Title']
    filter_backends = (SearchFilter, OrderingFilter)


class ProductDetails(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(UserId=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(UserId=self.request.user)


class OrderDetails(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Order.objects.filter(UserId=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(UserId=self.request.user)


class OrderItemList(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderItem.objects.filter(UserId=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(UserId=self.request.user)


class OrderItemDetails(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = (IsUser,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderItem.objects.filter(UserId=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(UserId=self.request.user)
