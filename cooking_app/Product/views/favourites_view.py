from rest_framework.response import Response
from Product.models import Favourite
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from Product.serializers import FavouriteModelSerializer


class FavouriteGenericView(generics.ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteModelSerializer


class FavouriteDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteModelSerializer