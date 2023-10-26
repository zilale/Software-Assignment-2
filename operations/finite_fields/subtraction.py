from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction as subtraction

# Finite field arithmetic subtraction
def finiteSubtraction(f, g, m, h):
    x = division(subtraction(f, g, m), h, m)
    return x[1]