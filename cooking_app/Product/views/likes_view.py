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


class LikesView(APIView):

    def get(self, request):
        likes = Likes.objects.all()
        serializer = LikesModelSerializer(likes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = LikesModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LikesDetailView(APIView):

    def get_likes_object(self, likes_id):
        try:
            likes = Likes.objects.get(id=likes_id)
        except Likes.DoesNotExist:
            return Response({"message": "Like does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return likes

    def delete(self, request, likes_id):
        self.get_likes_object(likes_id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)