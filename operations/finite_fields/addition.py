from operations.polynomial_arithmetic.polynomial_addition import addition 
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division

# Finite field arithmetic addition
def finiteAddition(f ,g, m, h):
        x = division(addition(f, g, m),h, m)
        return x[1]