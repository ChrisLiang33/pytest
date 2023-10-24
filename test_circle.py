import pytest
import shapes
import math

class TestCircle:
    def setup_method(self, method):
        print(f"setting up {method}") 
        self.circle = shapes.Circle(10)
    
    def teardown_method(self, method):
        print(f"tearing down {method}")
        del self.circle

    def test_radius(self):
        assert self.circle.radius() == math.pi ** self.circle.radius ** 2
    
    def test_perimeter(self):
        res = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert res == expected
    