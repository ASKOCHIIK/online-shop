from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.carts.models import Cart
from apps.carts.serializers import CartSerializer, CartCreateSerializer
from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        products = Product.objects.filter(product_carts__user=user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = CartCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDeleteAPIView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated, )

    def delete(self, request, id, *args, **kwargs):
        user = request.user
        try:
            cart = Cart.objects.get(product__id=id, user=user)
            cart.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)


