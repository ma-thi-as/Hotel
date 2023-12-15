from django.urls import path
from .views import (RoomCreateView, RoomListView, RoomDetailView, RoomUpdateView, RoomDeleteView,
                    Room_typeCreateView, Room_typeDeleteView, Room_typeDetailView, Room_typeListView, Room_typeUpdateView)

urlpatterns = [
    path("create/", RoomCreateView.as_view(), name="create"),
    path("list/", RoomListView.as_view(), name="list"),
    path("delete/<int:pk>/", RoomDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>/", RoomDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", RoomUpdateView.as_view(), name="update"),

    path("type-create/", Room_typeCreateView.as_view(), name="type_create"),
    path("type-list/", Room_typeListView.as_view(), name="type_list"),
    path("type-delete/<int:pk>/", Room_typeDeleteView.as_view(), name="type_delete"),
    path("type-detail/<int:pk>/", Room_typeDetailView.as_view(), name="type_detail"),
    path("type-update/<int:pk>/", Room_typeUpdateView.as_view(), name="type_update"),

]
