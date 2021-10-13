""" this module tests add_flower.py """

from src.utility.constants import STOCK


def test_add_to_stock(add):
    """ assert if the stocks are added """
    assert STOCK[0]['quantity'] == 20
    add[0].add_to_stock(10)
    assert STOCK[0]['quantity'] == 30
    STOCK[0]['quantity'] = 20


def test_add_new_in_stock(add):
    """ asserts if new items is added or not and also the correct value is added
    :param: add: it's a tuple of two objects of AddFlower, where add[0] = AddFLower("Sunflower")
    """
    length = len(STOCK)
    # here first parameter is for quantity and second for price while flower name is initialised already
    add[1].add_new_in_stock(10, 4.5)
    assert len(STOCK) == length + 1
    assert STOCK[-1] == {'flower_name': "Sunflower", 'quantity': 10, "price": 4.5}
    STOCK.pop()

