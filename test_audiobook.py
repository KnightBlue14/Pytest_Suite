import pytest
import functions
import time

def test_add():
    result = functions.add(1,4)
    assert result == 5

def test_div():
    result = functions.divide(10,5)
    assert result == 2


def test_burger():
    result = functions.add("I like"," burgers")
    assert result == "I like burgers"

def test_div_by_zero():
    with pytest.raises(ValueError):
        result = functions.divide(10,0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = functions.divide(10,5)
    assert result == 2

@pytest.mark.skip(reason='borked')
def test_add():
    assert functions.add(1,2) == 3

@pytest.mark.xfail(reason='div by 0')
def test_div0():
    assert functions.divide(4,0)