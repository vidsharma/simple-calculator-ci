import pytest
import calculator as calc

def test_add():

    assert(calc.add(2, 4) == 6)
    assert(calc.add(0, 4) == 4)
    assert(calc.add(2, -4) == -2)
    assert(abs(calc.add(1.2, 2000.4) - 2001.6) < 1e-10)
  

def test_mult():
    
    assert(calc.multiply(2,3) == 6)
