from django.urls import path

from cartapp.views import ProductList, ProductDetails, OrderItemDetails, OrderItemList, OrderList, OrderDetails

urlpatterns = [
    path('products/', ProductList.as_view({'get': 'list'}), name='productlist'),
    path('product/<str:pk>/',
         ProductDetails.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='productdetails'),
    path('orders/', OrderList.as_view({'get': 'list'}), name='orderlist'),
    path('orders/<str:pk>',
         OrderDetails.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='orderdetails'),
    path('orderitem/', OrderItemList.as_view({'get': 'list'}), name='orderitemlist'),
    path('orderitem/<str:pk>',
         OrderItemDetails.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='orderitemdetails'),

]
