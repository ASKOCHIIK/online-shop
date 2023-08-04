from django.urls import path
from apps.ratings.views import RatingCreateAPIView

urlpatterns = [
    path('create', RatingCreateAPIView.as_view(), name='rating-create'),
]