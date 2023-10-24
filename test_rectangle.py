import pytest
import shapes


# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10,20)

# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(5,6)
def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

def test_not_eq(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle