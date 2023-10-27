from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division, remove_leading_zeros

def extended_euclidean_algorithm(f, g, p):
    x, v, y, u = [1], [0], [0], [1]
    helper = False

    helper = any(val != 0 for val in g)

    while helper == True:

        q, r = polynomial_long_division(f, g, p)
        f = g
        g = r
        x_add = x
        y_add = y
        x = u
        y = v
        u = polynomial_subtraction(x_add, polynomial_multiplication(q, u, p), p)
        v = polynomial_subtraction(y_add, polynomial_multiplication(q, v, p), p)
        helper = False

        helper = any(val != 0 for val in g)

    lc_f = f[len(f) - 1]
    lc_f_inv = [pow(lc_f, -1, p)]
    
    
    a = polynomial_multiplication(x, lc_f_inv, p)
    b = polynomial_multiplication(y, lc_f_inv, p)
    remove_leading_zeros(a)
    remove_leading_zeros(b)

    gcd = (polynomial_multiplication(f,a,p),polynomial_multiplication(g,b,p),p)
    remove_leading_zeros(gcd)
    return a, b, gcd

def test_extended_euclidean_algorithm():
    # Test case 1
    f = [1, 1, 1]
    g = [1, 1]
    p = 5
    expected_a = [2, 3]
    expected_b = [4, 1]
    expected_gcd = ([1, 1], [1], 5)
    print(extended_euclidean_algorithm(f, g, p))
    assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)

    # Test case 2
    f = [1, 2, 1]
    g = [1, 1]
    p = 5
    expected_a = [3]
    expected_b = [2, 3]
    expected_gcd = ([1, 1], [1], 5)
    print(extended_euclidean_algorithm(f, g, p))
    assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)

    # Test case 3
    f = [1, 1, 1]
    g = [1, 1]
    p = 2
    expected_a = [1, 1]
    expected_b = [1]
    expected_gcd = ([1, 1], [1], 2)
    print(extended_euclidean_algorithm(f, g, p))
    assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)

    # Test case 4
    f = [1, 1, 1]
    g = [1, 1]
    p = 3
    expected_a = [1, 2]
    expected_b = [1]
    expected_gcd = ([1, 1], [1], 3)
    print(extended_euclidean_algorithm(f, g, p))
    assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)

# test_extended_euclidean_algorithm()