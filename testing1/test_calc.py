from pythoncode1.calcator import Calc
import pytest


@pytest.mark.add
def test_add1():
    calc1 = Calc()
    assert 2 == calc1.add(1, 2)


@pytest.mark.add
def test_add2():
    calc1 = Calc()
