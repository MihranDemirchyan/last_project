from rest_framework.response import Response
from Product.models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics
from Product.serializers import ProductModelSerializer


class ProductView(APIView):
    """
    endpoint will be products/
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        product_list = Product.objects.all()

        serializer = ProductModelSerializer(product_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id, user=request.user).first()

        if not product:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelSerializer(product)
        serializer.save(user=request.user)

        return Response(serializer.data)

    def patch(self, request, product_id):
        product = Product.objects.filter(id=product_id, user=request.user).first()

        if not product:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductModelSerializer(product)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request, product_id):
        product = Product.objects.filter(id=product_id, user=request.user).first()

        if not product:
            return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response(status.HTTP_204_NO_CONTENT)
