import pytest
from  list_items.models import List_items


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
    new_groc.groc_item = 'Pytest'
    new_groc.save()
    assert List_items.objects.filter(groc_item='Pytest').exists()

def test_delete_grocery(new_groc):
    new_groc.delete()
    assert (List_items.objects.filter(groc_item='Pytest').exists()) == False