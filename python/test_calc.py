import pytest
import calculator as calc

def test_add():

    assert(calc.add(2, 4) == 6)
    assert(calc.add(1.2, 2000.4) == 2001.6)
  

def test_mult():
    pass
