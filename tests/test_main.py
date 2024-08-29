# tests/test_main.py

import pytest
from my_module.main import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
