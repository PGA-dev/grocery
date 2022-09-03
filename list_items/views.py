from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import List_items

# Create your views here.
class List_itemsListView(ListView):
    model = List_items
    queryset = List_items.objects.all().order_by("-date_created")

class List_itemsDetailView(DetailView):
    model = List_items

#CRUD views

class List_itemsCreateView(CreateView):
    model = List_items
    fields = ["groc_item", "notes", "item_price", "budget"]
    success_url = reverse_lazy("list_items-list")

class List_itemsUpdateView(UpdateView):
    model = List_items
    fields = ["groc_item", "notes", "item_price", "budget"]

    def get_success_url(self):
        return reverse_lazy(
            "list_items-detail",
            kwargs={"pk": self.list_items.id}
        )

class List_itemsDeleteView(DeleteView):
    model = List_items
    success_url = reverse_lazy("list_items-list")