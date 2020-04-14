import datetime as dt

from app.shopping_cart import to_usd
from app.shopping_cart import human_friendly_timestamp
from app.shopping_cart import calculate_total_price



def test_to_usd():
    result = to_usd(3.4)
    assert result == "$3.40"


def test_human_friendly_timestamp():
    time = human_friendly_timestamp(dt.datetime.now())
    assert time == dt.datetime.now().strftime("%Y-%m-%d %H:%M")

def test_calculate_total_price():
    subtotal = 5
    tax = .5
    total = calculate_total_price(subtotal,tax)
    assert total == 5.50