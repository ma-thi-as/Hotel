from django.urls import path
from .views import PaymentCreateView, PaymentDeleteView, PaymentUpdateView, PaymentListView,PaymentDetailView

urlpatterns = [
    path("create/", PaymentCreateView.as_view(), name="create"),
    path("list/", PaymentListView.as_view(), name="list"),
    path("update/<int:pk>/", PaymentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PaymentDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", PaymentDetailView.as_view(), name="detail"),
]
