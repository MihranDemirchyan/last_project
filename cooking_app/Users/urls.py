from django.urls import path
from Users.views import user_view


urlpatterns = [
    path('', user_view.UserListCreateView.as_view()),
    path('<int:pk>/', user_view.UserRetrieveUpdateView.as_view()),
    path('verify_token', user_view.UserVerificationView.as_view()),
]