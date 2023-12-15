from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Payment
from django.urls import reverse_lazy
# Create your views here.


class PaymentCreateView(CreateView):
    model = Payment
    template_name = "create.html"
    fields = '__all__'
class PaymentListView(ListView):
    model = Payment
    template_name = "list.html"

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('payments:list')


class PaymentDetailView(DetailView):
    model = Payment
    template_name = "detail.html"

class PaymentUpdateView(UpdateView):
    model = Payment
    template_name = "update.html"
    fields = '__all__'

