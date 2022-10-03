import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_pass(self):
        assert self.calc.multiply(self, 5, 6) == 30

    def test_division_calculate_pass(self):
        assert self.calc.division(self, 300, 6) == 50

    def test_subtraction_calculate_pass(self):
        assert self.calc.subtraction(self, 500, 250) == 250

    def test_adding_calculate_pass(self):
        assert self.calc.adding(self, 130, 50) == 180

