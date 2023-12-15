from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import IndexView, CustomLoginView, UserCreateView,Customlogout, UrlHandlerView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("links", UrlHandlerView.as_view(), name="links"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", Customlogout, name="logout"),
    path("register/", UserCreateView.as_view(), name="register")
]
