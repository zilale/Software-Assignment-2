from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication as multiplication
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division

# Finite field arithmetic multiplication
def finiteFieldsMultiplication(f, g, m, h):
    x = division(multiplication(f, g, m), h, m)
    return x[1]