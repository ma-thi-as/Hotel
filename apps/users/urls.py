from django.urls import path
from .views import IndexView, CustomLoginView, UserCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", UserCreateView.as_view(), name="register")
]
