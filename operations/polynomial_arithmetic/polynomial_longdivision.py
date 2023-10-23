from polynomial_subtraction import polynomial_subtraction

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def inverse(num, p):
    g, x, _ = extended_gcd(num, p)
    return x % p
    

def multiply_polynomial_by_scalar(f, scalar, p):
    return [(x * scalar) % p for x in f]

def polynomial_long_division(f, g, p):
    
    q = [0] * max(1, len(f) - len(g) + 1)
    r = f[:]
    
    while len(r) >= len(g):
        leading_term_position = len(r) - len(g)
        factor = (r[-1] * inverse(g[-1], p)) % p
        q[leading_term_position] = factor

        subtract_term = multiply_polynomial_by_scalar(g, factor, p)
        subtract_term = [0] * leading_term_position + subtract_term
        r = polynomial_subtraction(r, subtract_term, p)
        
        while r and r[-1] == 0:
            r.pop()

    return q, r

f = [4, 0, -3, 1]  # Represents 4 - 3x^2 + x^3
g = [1, -1]  # Represents 1 - x
q, r = polynomial_long_division(f, g, 1000000007)
assert q == [1, 1, 1]  # x^2 + x + 1
assert r == [5]