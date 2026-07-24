"""
test_store_analytics.py

Starter file for the "write your own tests" exercise.

pytest and the module under test are already imported below, and there's
one fully-worked example test to show you the pattern. Everything after
that is up to you: add your own test functions (name them test_something)
that check store_analytics.py against its docstrings.

Run your tests from this folder with:
    pytest -v
"""

import pytest
from store_analytics import (
    parse_order_row,
    compute_line_total,
    summarize_by_product,
    top_n_products,
)


# --- Example test (already written for you) -------------------------------

def test_parse_order_row_valid_row():
    row = ["1001", "Widget", "4", "9.99", "alice@example.com"]
    order = parse_order_row(row)
    assert order == {
        "order_id": "1001",
        "product": "widget",
        "quantity": 4,
        "unit_price": 9.99,
        "customer_email": "alice@example.com",
    }


# --- Your tests go below here ----------------------------------------------
#Test totals
def test_compute_line_total():
    order = {'quantity': 3, 'unit_price': 10}
    result = compute_line_total(order)
    assert result == 30
#rounding problems
def test_compute_line_total_2():
    order = {'quantity': 3, 'unit_price': 2.33}
    result = compute_line_total(order)
    assert result == 6.99

# Test product info
def test_summarize_by_product_basic():
    orders = [
        {"product": "mug", "quantity": 2, "unit_price": 10.0},
        {"product": "mug", "quantity": 1, "unit_price": 10.0},
        {"product": "hat", "quantity": 1, "unit_price": 15.0},
    ]
    summary = summarize_by_product(orders)
#Test values, see if works
    assert summary["mug"]["total_quantity"] == 3
    assert summary["mug"]["total_revenue"] == 30.0
    assert summary["mug"]["order_count"] == 2

    assert summary["hat"]["total_quantity"] == 1
    assert summary["hat"]["total_revenue"] == 15.0
    assert summary["hat"]["order_count"] == 1
#If empty
def test_summarize_by_product_empty():
    orders = []
    summary = summarize_by_product(orders)
    assert summary == {}

#top products
def test_top_n_products_basic():
    summary = {
        'hat': {'total_revenue': 15},
        'mug': {'total_revenue': 30},
        'sticker': {'total_revenue': 5},
    }
    top = top_n_products(summary, n=2)
#High revenue first
    assert len(top) == 2 #added to make sure we get back only 2 products
    assert top[0][0] == "mug"
    assert top[1][0] == "hat"

#If we have a tie in revenue, sort Alphabetical
def test_top_n_products_tie_breaker():
    summary = {
        'zebra poster': {"total_revenue": 20},
        'apple sticker': {"total_revenue": 20},
    }
    top = top_n_products(summary, n=2)

    assert top[0][0] == 'apple sticker'
    assert top[1][0] == 'zebra poster'
