from django.urls import path
from apps.products.views import (
    ProductListAPIView, ProductRetrieveAPIView,
    ProductCreateAPIView, ProductUpdateAPIView,
    ProductDeleteAPIView, ProductOwnerAPIView
)

urlpatterns = [
    path('list', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('create', ProductCreateAPIView.as_view(), name='product-create'),
    path('update/<int:pk>', ProductUpdateAPIView.as_view(), name='product-update'),
    path('delete/<int:pk>', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('owners', ProductOwnerAPIView.as_view(), name='product-owners')
]
