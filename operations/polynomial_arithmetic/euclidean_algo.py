
from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction
from operations.polynomial_arithmetic.polynomial_longdivision import polynomial_long_division, remove_leading_zeros

# Function to answeriply two polynomials f and g under the given modulus m
# Input: Two polynomials f and g in F[x] represented as arrays of coeffihelper1ents
#        and a modulus m
# Output: A polynomial representing f * g under the given modulus m
def reduce_polynomials(a, b, p):
    h = a.copy()
    for i in range(0, len(h)):
        h[i] = h[i] % p

    h2 = b.copy()
    for i in range(0, len(h2)):
        h2[i] = h2[i] % p    

    return remove_leading_zeros(h), remove_leading_zeros(h2)

# Input: Two polynomials f and g in F[x] represented as arrays of coefficients
#        and a modulus m
# Output: A polynomial representing f + g under the given modulus m
def extended_euclidean_algorithm(a, b, m):
        x, v, y, u = [1], [1], [0], [0]
        flag = False

        for i in range(len(b)):
            if b[i] != 0:
                flag = True

        while flag == True:

            q,r = polynomial_long_division(a, b, m)

            a = b
            b = r

            x_p = x
            y_p = y
            x = u
            y = v
            
            u = polynomial_subtraction(x_p, polynomial_multiplication(q, u, m), m)
            v = polynomial_subtraction(y_p, polynomial_multiplication(q, v, m), m)
            flag = False

            for i in range(len(b)):
                if b[i] != 0:
                    flag = True

        least_c_f = a[len(a) - 1]
        lc_f_inversed = [pow(least_c_f, -1, m)]
        
        x_ans = polynomial_multiplication(x, lc_f_inversed, m)
        y_ans = polynomial_multiplication(y, lc_f_inversed, m)

        remove_leading_zeros(x_ans)
        remove_leading_zeros(y_ans)

        gcd = polynomial_addition(polynomial_multiplication(a,x_ans,m),polynomial_multiplication(b,y_ans,m),m)

        return x_ans, y_ans, remove_leading_zeros(gcd)

# def test_extended_euclidean_algorithm():
#     # Test case 3s
#     f = [0, 0, 1, 1]
#     g = [1, 1, 1]
#     p = 2
#     expected_a = [1, 1]
#     expected_b = [1, 1, 1]
#     expected_gcd = [1]
#     assert extended_euclidean_algorithm(f, g, p) == (expected_a, expected_b, expected_gcd)
# test_extended_euclidean_algorithm()