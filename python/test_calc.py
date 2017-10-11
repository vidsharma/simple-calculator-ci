import pytest
import calculator as calc

def test_add():

    assert(calc.add(2, 4) == 6)
    assert(calc.add(0, 4) == 4)
    assert(calc.add(2, -4) == -2)
    assert(abs(calc.add(1.2, 2000.4) - 2001.6) < 1e-10)
  


@pytest.mark.parametrize("arg1,arg2,out",
    [ (2,3,6),
    (0.1,6,pytest.approx(0.6)),
    (-4,5,-20),
    (0,123,0)])

def test_mult(arg1, arg2, out):
    assert(calc.multiply(arg1, arg2) == out)
    with pytest.raises(Exception,
             message = 'Exception for non-numerical argument'):
        calc.multiply('NaN',0)
