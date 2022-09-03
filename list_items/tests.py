from django.test import TestCase
from django.urls import reverse
import pytest
from  list_items.models import List_items

#**********tests for acccess and routing**********

def test_homepage_access():
    url = reverse('list_items-list')
    assert url == "/"


#*****************tests for CRUD******************

#fixture for db access
@pytest.fixture
def new_groc(db):
    listitem = List_items.objects.create(
        groc_item='Pytest',
        notes='pytest',
        item_price=10,
        budget=10
    )
    return listitem

#actual CRUD tests
def test_search_grocery(new_groc):
    assert List_items.objects.filter(groc_item='Pytest').exists()

def test_update_grocery(new_groc):
    new_groc.groc_item = 'Pytest-Django'
    new_groc.save()
    assert List_items.objects.filter(groc_item='Pytest-Django').exists()

def test_delete_grocery(new_groc):
    new_groc.delete()
    assert (List_items.objects.filter(groc_item='Pytest-Django').exists()) == False