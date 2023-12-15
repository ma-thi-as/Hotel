from django.shortcuts import render
from django.views.generic import UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Employee, Guest
from .forms import EmployeeForm

# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    template_name = "emp/list.html"

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "emp/update.html"
    
    def get_success_url(self):
        return reverse_lazy('persons:emp_detail', kwargs={'pk': self.kwargs['pk']})    

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "emp/detail.html"

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "emp/confirm_delete.html"


class GuestListView(ListView):
    model = Guest
    template_name = "guest/list.html"

class GuestUpdateView(UpdateView):
    model = Guest
    form_class = EmployeeForm
    template_name = "guest/update.html"
    
    def get_success_url(self):
        return reverse_lazy('persons:guest_detail', kwargs={'pk': self.kwargs['pk']})    

class GuestDetailView(DetailView):
    model = Guest
    template_name = "guest/detail.html"

class GuestDeleteView(DeleteView):
    model = Guest
    template_name = "guest/confirm_delete.html"
