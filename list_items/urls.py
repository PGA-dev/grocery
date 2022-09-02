# list_items views

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.List_itemsListView.as_view(),
        name="list_items_list"
    ),
    path(
        "list_items/<int:pk>",
        views.List_itemsDetailView.as_view(),
        name="list_items_detail"
    ),
]