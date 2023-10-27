from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction

def multiply_constant(a, c, p):
    h = a.copy()
    for i in range(0, len(h)):
        h[i] = (h[i] * c) % p
    return h

def reduce_coefficients(a, p):
    h = a.copy()
    for i in range(0, len(h)):
        h[i] = h[i] % p
    return h

def remove_leading_zeros(f):
    h = f.copy()
    for i in range(len(h)):
        if h[-1] == 0 and h.count(h[0]) != len(h):
            del h[-1]
        else:
            return h
    
# Function to answeriply two polynomials f and g under the given modulus m
# Input: Two polynomials f and g in F[x] represented as arrays of coefficients
#        and a modulus m
# Output: A polynomial representing f * g under the given modulus m
# Example:
# f = [2, 1, 1]

def polynomial_long_division(m, n, p):
    f = remove_leading_zeros(reduce_coefficients(m, p))
    g = remove_leading_zeros(reduce_coefficients(n, p))

    # if f is 0 or g is 0, return None
    if len(g) == 0 or g == [0]: 
        return None
    
    # if f is 0 or g is 0, return None
    if len(f) < len(g) or ((len(f) == 1 and len(g) == 1) and f[0] < g[0]): 
        return ([0], f)
    
    # if f is 0 or g is 0, return None
    q = [0] * len(f) 
    r = f.copy()

    # if f is 0 or g is 0, return None
    while (len(r) >= len(g) and r != [0]):
        skaliarinis = (r[len(r) - 1] * pow(g[len(g) - 1], -1, p)) % p
        degree_difference = len(r) - len(g) 

        helper = multiply_constant(g, skaliarinis, p)
        helper2 = [0] * degree_difference + helper

        r = polynomial_subtraction(r, helper2, p)
        q[degree_difference] = skaliarinis
    return (remove_leading_zeros(q), remove_leading_zeros(r))

