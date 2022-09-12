from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

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

# Basic frontend views.
class List_itemsListView(ListView):
    model = List_items
    queryset = List_items.objects.all().order_by("groc_item").values()


class List_itemsDetailView(DetailView):
    model = List_items

#CRUD views

class List_itemsCreateView(SuccessMessageMixin, CreateView):
    model = List_items
    fields = ["groc_item", "notes", "item_price", "budget"]
    success_url = reverse_lazy("list_items-list")
    success_message = "Your new grocery list item is created!"

class List_itemsUpdateView(SuccessMessageMixin, UpdateView):
    model = List_items
    fields = ["groc_item", "notes", "item_price", "budget"]
    success_message = "Your grocery list item has been updated!"

    def get_success_url(self):
        return reverse_lazy(
            "list_items-detail",
            kwargs={"pk": self.object.pk}
        )

class List_itemsDeleteView(DeleteView):
    model = List_items
    success_url = reverse_lazy("list_items-list")
    success_message = "Your grocery item was deleted!"

    def delete(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return super().delete(request, *args, **kwargs)