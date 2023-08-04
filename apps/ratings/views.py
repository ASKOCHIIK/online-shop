from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.ratings.models import Rating
from apps.ratings.serializers import RatingCreateSerializer
from apps.products.models import Product


class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RatingCreateSerializer(data=data)
        try:
            if serializer.is_valid():
                user = request.user
                rating = data['rating']
                product = Product.objects.get(id=data['product'])

                rating_obj = Rating.objects.filter(user=user, product=product).first()
                if rating_obj:
                    rating_obj.rating = rating
                    rating_obj.save()
                else:
                    Rating.objects.create(user=user, product=product, rating=rating)

                ratings = Rating.objects.filter(product=product).values_list('rating', flat=True)
                product.rating = sum(ratings) / len(ratings)
                product.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


