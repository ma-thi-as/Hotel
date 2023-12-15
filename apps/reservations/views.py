from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Reservation, CheckInOut
# Create your views here.

class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "create.html"
    fields = '__all__'

class ReservationListView(ListView):
    model = Reservation
    template_name = "list.html"

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "detail.html"

class ReservationUpdateView(UpdateView):
    model = Reservation
    template_name = "update.html"
    fields = '__all__'

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = "confirm_delete.html"




class CheckInOutCreateView(CreateView):
    model = CheckInOut
    template_name = "check/create.html"
    fields = '__all__'

class CheckInOutListView(ListView):
    model = CheckInOut
    template_name = "check/list.html"

class CheckInOutDetailView(DetailView):
    model = CheckInOut
    template_name = "check/detail.html"

class CheckInOutUpdateView(UpdateView):
    model = CheckInOut
    template_name = "check/update.html"
    fields = '__all__'

class CheckInOutDeleteView(DeleteView):
    model = CheckInOut
    template_name = "check/confirm_delete.html"
    success_url = reverse_lazy('reservations:check_list')
