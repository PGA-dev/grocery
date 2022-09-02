from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import List_items

# Create your views here.
class List_itemsListView(ListView):
    model = List_items
    queryset = List_items.objects.all().order_by("-date_created")

class List_itemsDetailView(DetailView):
    model = List_items
