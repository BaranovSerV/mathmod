from mathmod.approximation.linear_spline import linear_spline
from mathmod.approximation.ermit import ermit_polynomial
from mathmod.approximation.newton_devided import newton_devided, devided_differences
from mathmod.approximation.newton_finite import newton_finite, finite_differences
from mathmod.approximation.quadratic_spline_with_condition import quadratic_spline_with_an_additional_condition
from mathmod.approximation.fundamental_cubic_spline import (
    compute_fundamental_cubic_spline_coeffs,
    fundamental_cubic_spline
)

__all__ = [
    "linear_spline", 
    "ermit_polynomial",
    "newton_devided",
    "devided_differences",
    "newton_finite",
    "finite_differences",
    "quadratic_spline_with_an_additional_condition",
    "compute_fundamental_cubic_spline_coeffs",
    "fundamental_cubic_spline"
]