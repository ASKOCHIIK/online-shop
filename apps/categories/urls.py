from django.urls import path
from apps.categories.views import CategoryListAPIView, CategoryCreateAPIView, CategoryRetrieveAPIView

urlpatterns = [
    path('list', CategoryListAPIView.as_view(), name='category-list'),
    path('create', CategoryCreateAPIView.as_view(), name='category-create'),
    path('detail/<int:pk>', CategoryRetrieveAPIView.as_view(), name='category-detail')
]