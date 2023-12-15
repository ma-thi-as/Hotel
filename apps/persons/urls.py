from django.urls import path
from .views import (EmployeeListView, EmployeeDetailView, EmployeeDeleteView, EmployeeUpdateView,
                    GuestListView,GuestDetailView, GuestDeleteView, GuestUpdateView)
urlpatterns = [
    path("list/", EmployeeListView.as_view(), name="emp_list"),
    path("detail/<int:pk>/", EmployeeDetailView.as_view(), name="emp_detail"),
    path("update/<int:pk>/", EmployeeUpdateView.as_view(), name="emp_update"),
    path("delete/<int:pk>/", EmployeeDeleteView.as_view(), name="emp_delete"),

    path("guest_list/",GuestListView.as_view(), name="guest_list"),
    path("guest_detail/<int:pk>/", GuestDetailView.as_view(), name="guest_detail"),
    path("guest_update/<int:pk>/", GuestUpdateView.as_view(), name="guest_update"),
    path("guest_delete/<int:pk>/", GuestDeleteView.as_view(), name="guest_delete"),

]
