"""
Unit tests for the Scientific Calculator.
Run with: python -m pytest tests/ -v
"""

import math
import pytest
from calculator import (
    add, subtract, multiply, divide, modulo, power, floor_divide,
    square_root, nth_root, logarithm, log10, log2, exponential,
    absolute, factorial, ceiling, floor, round_to,
    sine, cosine, tangent, arcsine, arccosine, arctangent,
    degrees_to_radians, radians_to_degrees,
    sinh, cosh, tanh,
)


# ── Basic Operations ──────────────────────────────────────────────────────────

class TestBasicOperations:
    def test_add(self):
        assert add(3, 4) == 7
        assert add(-1, 1) == 0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self):
        assert subtract(10, 4) == 6
        assert subtract(0, 5) == -5

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 999) == 0

    def test_divide(self):
        assert divide(10, 2) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)

    def test_modulo(self):
        assert modulo(10, 3) == 1
        assert modulo(9, 3) == 0

    def test_modulo_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            modulo(5, 0)

    def test_power(self):
        assert power(2, 10) == 1024
        assert power(9, 0.5) == pytest.approx(3.0)

    def test_floor_divide(self):
        assert floor_divide(10, 3) == 3
        assert floor_divide(9, 3) == 3


# ── Scientific Operations ─────────────────────────────────────────────────────

class TestScientificOperations:
    def test_square_root(self):
        assert square_root(9) == pytest.approx(3.0)
        assert square_root(2) == pytest.approx(math.sqrt(2))

    def test_square_root_negative(self):
        with pytest.raises(ValueError):
            square_root(-1)

    def test_nth_root(self):
        assert nth_root(8, 3) == pytest.approx(2.0)
        assert nth_root(16, 4) == pytest.approx(2.0)

    def test_logarithm_natural(self):
        assert logarithm(math.e) == pytest.approx(1.0)
        assert logarithm(1) == pytest.approx(0.0)

    def test_log10(self):
        assert log10(100) == pytest.approx(2.0)
        assert log10(1) == pytest.approx(0.0)

    def test_log2(self):
        assert log2(8) == pytest.approx(3.0)

    def test_logarithm_invalid(self):
        with pytest.raises(ValueError):
            logarithm(0)
        with pytest.raises(ValueError):
            logarithm(-5)

    def test_exponential(self):
        assert exponential(0) == pytest.approx(1.0)
        assert exponential(1) == pytest.approx(math.e)

    def test_absolute(self):
        assert absolute(-7) == 7
        assert absolute(3) == 3
        assert absolute(0) == 0

    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_ceiling_floor(self):
        assert ceiling(4.1) == 5
        assert floor(4.9) == 4
        assert ceiling(-1.1) == -1
        assert floor(-1.1) == -2

    def test_round_to(self):
        assert round_to(3.14159, 2) == 3.14
        assert round_to(2.5) == 2  # banker's rounding


# ── Trigonometry ──────────────────────────────────────────────────────────────

class TestTrigonometry:
    def test_sine(self):
        assert sine(0) == pytest.approx(0.0)
        assert sine(math.pi / 2) == pytest.approx(1.0)

    def test_cosine(self):
        assert cosine(0) == pytest.approx(1.0)
        assert cosine(math.pi) == pytest.approx(-1.0)

    def test_tangent(self):
        assert tangent(0) == pytest.approx(0.0)
        assert tangent(math.pi / 4) == pytest.approx(1.0)

    def test_arcsine(self):
        assert arcsine(0) == pytest.approx(0.0)
        assert arcsine(1) == pytest.approx(math.pi / 2)

    def test_arcsine_out_of_range(self):
        with pytest.raises(ValueError):
            arcsine(1.5)

    def test_arccosine(self):
        assert arccosine(1) == pytest.approx(0.0)
        assert arccosine(0) == pytest.approx(math.pi / 2)

    def test_arctangent(self):
        assert arctangent(0) == pytest.approx(0.0)
        assert arctangent(1) == pytest.approx(math.pi / 4)

    def test_deg_rad_conversion(self):
        assert degrees_to_radians(180) == pytest.approx(math.pi)
        assert radians_to_degrees(math.pi) == pytest.approx(180.0)


# ── Hyperbolic Functions ──────────────────────────────────────────────────────

class TestHyperbolic:
    def test_sinh(self):
        assert sinh(0) == pytest.approx(0.0)

    def test_cosh(self):
        assert cosh(0) == pytest.approx(1.0)

    def test_tanh(self):
        assert tanh(0) == pytest.approx(0.0)
