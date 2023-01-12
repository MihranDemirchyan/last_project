from django.urls import path
from Product.views import (
    product_view, cuisine_view,
    elements_view, comments_view,
    likes_view, favourites_view
)

urlpatterns = [
    path('products/', product_view.ProductView.as_view()),
    path('products/<int:product_id>/', product_view.ProductDetailView.as_view()),
    path('cuisine/', cuisine_view.CuisineView.as_view()),
    path('elements/', elements_view.ElementsView.as_view()),
    path('elements/<int:elements_id>/', elements_view.ElementsDetailView.as_view()),
    path('comments/', comments_view.CommentsView.as_view()),
    path('comments/<int:comments_id>/', comments_view.CommentsDetailView.as_view()),
    path('likes/', likes_view.LikesView.as_view()),
    path('likes/<int:likes_id>/', likes_view.LikesDetailView.as_view()),
    path('favs/', favourites_view.FavouriteGenericView.as_view()),
    path('favs/<int:pk>/', favourites_view.FavouriteDetailGenericView.as_view()),
]