from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition 
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division

# Finite field arithmetic addition
def finite_fields_addition(f ,g, m, h):
        x = division(polynomial_addition(f, g, m),h, m)
        return x[1]

# Test
f = [1, 1, 1, 1, 1, 1]
g = [1, 1, 1, 1, 1, 1]
m = 2
h = [1, 1, 1, 1, 1, 1]
print(finite_fields_addition(f, g, m, h))