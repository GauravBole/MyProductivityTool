from django.urls import path

from .views import LoginApiView, UserRegisterApiView, UserDetailApiView
app_name = "userauth"
urlpatterns = [
    path('user_login/', LoginApiView.as_view(), name="user_login"),
    path('user_register/', UserRegisterApiView.as_view(), name="user_register"),
    path('user_detail/', UserDetailApiView.as_view(), name="user_detail")
]