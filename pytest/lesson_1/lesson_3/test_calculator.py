import pytest
import calculator


class TestCalculator:

    @pytest.mark.parametrize(
        'a, b', [
            (1, 2),
            (0, 0),
            (-1, 1),
            (-3, -7),
            (1.2, 3.6)
        ]
    )
    def test_addition(self, a, b):
        addition_result = calculator.addition(a, b)
        return addition_result

    @pytest.mark.parametrize(
        'a, b', [
            (1, 2),
            (0, 0),
            (-1, 1),
            (-3, -7),
            (1.2, 3.6)
        ]
    )
    def test_subtraction(self, a, b):
        subtraction_result = calculator.subtraction(a, b)
        return subtraction_result

    @pytest.mark.parametrize(
        'a, b', [
            (1, 2),
            (0, 0),
            (-1, 1),
            (10, 2),
            (1.4, 0.89)
        ]
    )
    def test_division(self, a, b):
        division_result = calculator.division(a, b)
        return division_result


    @pytest.mark.parametrize(
        'a, b', [
            (1, 2.8),
            (0, 0),
            (-1, 1),
            (10, 2),
            (1.4, 0.89)
        ]
    )
    def test_multiplication(self, a, b):
        multiplication_result = calculator.multiplication(a, b)
        return multiplication_result