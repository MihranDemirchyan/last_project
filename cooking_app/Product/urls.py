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
    path('comments/', comments_view.CommentsListView.as_view()),
    path('comments_create/', comments_view.CommentsCreateView.as_view()),
    path('comments/<int:comments_id>/', comments_view.CommentsDetailView.as_view()),
    path('likes_get/', likes_view.GetLikesView.as_view()),
    path('likes_put/', likes_view.PutLikesView.as_view()),
    path('likes/<int:likes_id>/', likes_view.LikesDetailView.as_view()),
    path('favs_list/', favourites_view.FavouriteListView.as_view()),
    path('favs_add/', favourites_view.AddToFavouriteView.as_view()),
    path('favs/<int:favourite_id>/', favourites_view.FavouritesDetailView.as_view()),
]