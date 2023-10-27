from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction

def multiply_constant(a, c, p):
    if a == None:
        return []
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
    
def multiply_n(f: list, n: int):
    return [0]*n + f

def polynomial_long_division(m: list, n: list, p: int):
    f = remove_leading_zeros(reduce_coefficients(m, p))
    g = remove_leading_zeros(reduce_coefficients(n, p))
    if len(g) == 0 or g == [0]: # Division by zero or an empty polynomial
        return None
    if len(f) < len(g) or ((len(f) == 1 and len(g) == 1) and f[0] < g[0]): 
        #f is of a smaller degree than g or they are both constants and f is smaller than g
        return ([0], f)
    q = [0] * len(f) # A maximum size list for the quotient of all zeros
    r = f.copy()
    while (len(r) >= len(g) and r != [0]):
        #scalar =  lc(r) * (lc(g))^(-1)
        scalar = (r[len(r) - 1] * pow(g[len(g) - 1], -1, p)) % p
        degree_difference = len(r) - len(g) 
        # r = r - X^(degree_difference) * g * scalar
        r = polynomial_subtraction(r, multiply_n(multiply_constant(g, scalar, p), degree_difference),p)
        q[degree_difference] = scalar # q = q + scalar*X^(degree_difference)
    return (remove_leading_zeros(q), remove_leading_zeros(r))

