from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division as division

# Finite field arithmetic division
def finite_fields_division(f, g, m, h):
    q, r = division(f, g, m)
    z, r = division(q, h, m)
    return z