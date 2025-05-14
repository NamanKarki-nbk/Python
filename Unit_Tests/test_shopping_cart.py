from shoppingcart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock

import pytest


@pytest.fixture
def cart():
    #All setup for the cart here...
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    
    cart.add("apple")
    assert cart.size() == 1  #assert check ithe given statement is true or not if its false the test fails
    
    
def test_when_item_added_then_cart_contains_item(cart):
    
    cart.add("apple")
    assert "apple" in cart.get_items()
    
    
def test_when_add_more_than_max_items_should_fail(cart):
    
    for _ in range(5):
        cart.add("mango")
    with pytest.raises(OverflowError):   # what ever i run below this line it expects it to throw this error and if does throw this error then this test passes
        cart.add("apple")
    

def test_can_get_total_price(cart):
    print("Testing can get price") #pytest test_shopping_cart.py::test_can_get_total_price -s yeslai chai specific method for testing run garcha ani with the flag -s we can runt he print statement
   
    cart.add("apple")
    cart.add("orange")
    
    item_database = ItemDatabase()
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0
        
    item_database.get = Mock(side_effect= mock_get_item)
    assert cart.get_total_price(item_database) == 3.0 
    