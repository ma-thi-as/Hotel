from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Room, Room_type
from .forms import RoomForm
from apps.users.mixins import StaffOrAdminMixin
# Create your views here.



class RoomCreateView(CreateView):
    model = Room
    template_name = "create.html"
    form_class = RoomForm

class RoomListView(StaffOrAdminMixin, ListView):
    model = Room
    template_name = "list.html"

class RoomDetailView(DetailView):
    model = Room
    template_name = "detail.html"

class RoomUpdateView(UpdateView):
    model = Room
    template_name = "update.html"
    form_class = RoomForm
    
class RoomDeleteView(DeleteView):
    model = Room
    template_name = "confirm_delete.html"



class Room_typeCreateView(CreateView):
    model = Room_type
    template_name = "type/create.html"
    fields = '__all__'

class Room_typeListView(ListView):
    model = Room_type
    template_name = "type/list.html"

class Room_typeDetailView(DetailView):
    model = Room_type
    template_name = "type/detail.html"

class Room_typeUpdateView(UpdateView):
    model = Room_type
    template_name = "type/update.html"
    fields = '__all__'
    
class Room_typeDeleteView(DeleteView):
    model = Room_type
    template_name = "type/confirm_delete.html"


