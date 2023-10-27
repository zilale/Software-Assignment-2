from operations.polynomial_arithmetic.euclidean_algo import extended_euclidean_algorithm

# Finite field arithmetic inverse
def finite_fields_inversion(f, m, h):
        a, b, gcd = extended_euclidean_algorithm(f,h,m)
        return a