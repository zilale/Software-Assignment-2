
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction
from operations.polynomial_arithmetic.polynomial_longdivision import multiply_constant, polynomial_long_division, reduce_coefficients, remove_leading_zeros

def reduce_polynomials(a, b, p):
    h = a.copy()
    for i in range(0, len(h)):
        h[i] = h[i] % p

    h2 = b.copy()
    for i in range(0, len(h2)):
        h2[i] = h2[i] % p    

    return remove_leading_zeros(h), remove_leading_zeros(h2)

def extended_euclidean_algorithm(f, g, p):
    a, b = reduce_coefficients(f, p), reduce_coefficients(g, p)
    switch = False
    switch = len(a) < len(b) or (len(a) == len(b) and a[::-1] < b[::-1])
    if switch:
        a, b = b, a

    x = [1]
    v = [1]
    y = [0]
    u = [0]

    # if f is 0 or g is 0, return None
    while b != [0]:
        q, r = polynomial_long_division(a, b, p)
        a = b.copy()
        b = r.copy()
        x_p = x.copy()
        y_p = y.copy()
        x = u.copy()
        y = v.copy()
        u = polynomial_subtraction(x_p, polynomial_multiplication(q, u, p), p)
        v = polynomial_subtraction(y_p, polynomial_multiplication(q, v, p), p)
    
    lc_a = a[len(a) - 1]
    lc_a_inversed = pow(lc_a, -1, p)


    x_final = multiply_constant(x, lc_a_inversed, p)
    y_final = multiply_constant(y, lc_a_inversed, p)
    gcd = multiply_constant(a, lc_a_inversed, p)
    

    if switch:
        x_final, y_final = y_final, x_final

    return x_final, y_final, gcd

def test_extended_euclidean_algorithm():
    # Test case 3s
    f = [0, 0, 1, 1]
    g = [1, 1, 1]
    p = 2
    expected_a = [1, 1]
    expected_b = [1, 1, 1]
    expected_gcd = [1]
    assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)
# test_extended_euclidean_algorithm()