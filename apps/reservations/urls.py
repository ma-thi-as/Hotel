from django.urls import path 
from .views import (ReservationCreateView, ReservationDeleteView, ReservationDetailView, ReservationListView, ReservationUpdateView,
                    CheckInOutCreateView, CheckInOutDeleteView, CheckInOutUpdateView, CheckInOutListView, CheckInOutDetailView)
urlpatterns = [
    path("create/", ReservationCreateView.as_view(), name="create"),
    path("list/", ReservationListView.as_view(), name="list"),
    path("update/<int:pk>/", ReservationUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/", ReservationDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", ReservationDeleteView.as_view(), name="delete"),


    path("check-create/", CheckInOutCreateView.as_view(), name="check_create"),
    path("check-list/", CheckInOutListView.as_view(), name="check_list"),
    path("check-update/<int:pk>/", CheckInOutUpdateView.as_view(), name="check_update"),
    path("check-detail/<int:pk>/", CheckInOutDetailView.as_view(), name="check_detail"),
    path("check-delete/<int:pk>/", CheckInOutDeleteView.as_view(), name="check_delete"),

]
