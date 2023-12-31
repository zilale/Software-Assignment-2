from operations.polynomial_arithmetic.euclidean_algo import extended_euclidean_algorithm
def irreducibility_check(f, p):
    n = len(f) - 1  # Degree of the polynomial
    t = 1
    while t < n:
        sum_poly = [0] * (p ** t + 1)
        sum_poly[p ** t] = 1
        sum_poly[1] = -1

        x, y, gcd_coeffs = extended_euclidean_algorithm(f, sum_poly, p)

        # Check if the gcd is 1 and all other coefficients are 0
        if len(gcd_coeffs) == 1 and gcd_coeffs[0] == 1:
            return True  # Polynomial is reducible
        elif all(coeff == 0 for i, coeff in enumerate(gcd_coeffs) if i != 0):
            return False  # Polynomial is irreducible

        t += 1

    return False  # If we reach this point, the polynomial is irreducible

