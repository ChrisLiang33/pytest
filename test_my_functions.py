import pytest
import my_function
import time

def test_add():
    res = my_function.add(1,4)
    assert res == 5

def test_divide():
    res = my_function.divide(10,5)
    assert res == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_function.divide(10,0)

def test_add_strings():
    res = my_function.add('i like ', 'food')
    assert res == 'i like food'

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    res = my_function.divide(10,5)
    assert res == 2

@pytest.mark.skip(reason='broken currently')
def test_add():
    assert my_function.add(1,2)==3

@pytest.mark.xfail(reason='canot divide by zereo')
def test_devidde_by_zero():
    my_function.divide(4,0)
