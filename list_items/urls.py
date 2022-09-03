# list_items views

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.List_itemsListView.as_view(),
        name="list_items-list"
    ),
    path(
        "list_items/<int:pk>",
        views.List_itemsDetailView.as_view(),
        name="list_items-detail"
    ),
    path(
        "create",
        views.List_itemsCreateView.as_view(),
        name="list_items-create"
    ),
    path(
        "list_items/<int:pk>/update",
        views.List_itemsUpdateView.as_view(),
        name="list_items-update",
    ),
    path(
        "list_items/<int:pk>/delete",
        views.List_itemsDeleteView.as_view(),
        name="list_items-delete",
    ),
]