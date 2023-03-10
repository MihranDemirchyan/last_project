from rest_framework import serializers
from Product.models import (
    Product, Elements,
    Cuisine, Likes,
    Comments, Favourite
)
from Users.serializers import UserSerializer


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("id", "product_name", "user", "cuisine", "product_elements")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(data)
        data["user"] = UserSerializer(instance.user).data

        return data


class CuisineModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuisine
        fields = "__all__"


class ElementsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = "__all__"

    # def to_representation(self, instance):
    #     return {
    #         "name": instance.name
    #     }


class LikesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = "__all__"


class CommentsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"


class FavouriteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"