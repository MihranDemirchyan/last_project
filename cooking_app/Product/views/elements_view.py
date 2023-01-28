from rest_framework.response import Response
from Product.models import (
    Elements,
    Comments, Likes,
    Favourite, Cuisine
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from Product.serializers import (
    ProductModelSerializer, ElementsModelSerializer,
    CommentsModelSerializer, LikesModelSerializer,
    CuisineModelSerializer, FavouriteModelSerializer
)


class ElementsView(APIView):
    """
    the endpoint will be elements/
    """

    def get(self, request):
        elements = Elements.objects.all()
        serializer = ElementsModelSerializer(elements, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ElementsModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ElementsDetailView(APIView):

    def get_elements_object(self, elements_id):
        try:
            elements = Elements.objects.get(id=elements_id)
        except Elements.DoesNotExist:
            return Response({"message": "Elements do not exist"}, status=status.HTTP_404_NOT_FOUND)
        return elements

    def get(self, request, elements_id):

        elements = self.get_elements_object(elements_id)

        serializer = ElementsModelSerializer(elements)

        return Response(serializer.data)

    def patch(self, request, elements_id):
        elements = self.get_elements_object(elements_id)

        serializer = ElementsModelSerializer(elements, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, elements_id):

        self.get_elements_object(elements_id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)