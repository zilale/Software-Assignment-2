from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division

# Finite field arithmetic division
def finiteFieldsDivision(f, g, m, h):
    q = division(f, g, m)
    z = division(q, h, m)
    return z