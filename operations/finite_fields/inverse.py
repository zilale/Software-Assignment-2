from operations.polynomial_arithmetic.euclidean_algo import extended_euclidean_algo

# Finite field arithmetic inverse
def finiteFieldsInverse(f, m, h):
        x, y, gcd = extended_euclidean_algo(f,h,m)
        return x