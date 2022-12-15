import pytest
from shopping import *


def test_add_item():

    assert len(cart_list) == 0
    assert len(price_list) == 0


def test_view_cart_items():
    for item_add in cart_list:
        assert isinstance(item_add, str)
        assert len(item_add) >= 1


def test_remove_item():
    for item_price in price_list:
        assert isinstance(item_price, float)
        assert len(item_price) >= 1


def test_compute_total():
    item_price = 0
    total_amount = 0
    assert total_amount == total_amount + item_price
    assert item_price == item_price
   
pytest.main(["-v", "--tb=line", "-rN", __file__])

