from rest_framework import serializers
from apps.ratings.models import Rating


class RatingCreateSerializer(serializers.ModelSerializer):
    rating = serializers.ChoiceField(choices=Rating.RATING_CHOICES)

    class Meta:
        model = Rating
        fields = ('product', 'rating')

