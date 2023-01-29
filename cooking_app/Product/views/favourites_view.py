from rest_framework.response import Response
from Product.models import Favourite
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from Product.serializers import FavouriteModelSerializer
from rest_framework.permissions import IsAuthenticated


class FavouriteListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        favourites = Favourite.objects.get()
        serializer = FavouriteModelSerializer(favourites)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToFavouriteView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FavouriteModelSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FavouritesDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, favourite_id):
        try:
            Favourite.objects.get(id=favourite_id).delete()
        except Favourite.DoesNotExist:
            return Response({"message": "There is not post like this"}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)
