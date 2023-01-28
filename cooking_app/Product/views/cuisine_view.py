from rest_framework.response import Response
from Product.models import Cuisine
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from Product.serializers import CuisineModelSerializer


class CuisineView(APIView):

    def get(self, request):

        cuisine = Cuisine.objects.all()
        serializer = CuisineModelSerializer(cuisine, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = CuisineModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ?
# class CuisineDetailView(APIView):
#
#     def get_cuisine_object(self, cuisine_id):
#         try:
#             cuisine = Cuisine.objects.get(id=cuisine_id)
#         except Cuisine.DoesNotExist:
#             return Response({"message": "Cuisine does not exist"}, status=status.HTTP_404_NOT_FOUND)
#         return cuisine
#
#     def get(self, request, cuisine_id):
#         cuisine = self.get_cuisine_object(cuisine_id)
#
#         serializer = CuisineModelSerializer(cuisine)
#
#         return Response(serializer.data)
#
#     def patch(self, request, cuisine_id):
#         cuisine = self.get_cuisine_object(cuisine_id)
#
#         serializer = CuisineModelSerializer(cuisine)
#
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, cuisine_id):
#         self.get_cuisine_object(cuisine_id).delete()
#
#         return Response(status=status.HTTP_204_NO_CONTENT)
