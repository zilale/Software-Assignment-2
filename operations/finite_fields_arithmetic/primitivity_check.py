from operations.finite_fields_arithmetic.multiplication import finite_fields_multiplication as multiplication

def find_prime_factors(n):
    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def primitivity_checking(f, m, h):
    q = m**(len(h) - 1)
    pf = find_prime_factors(q-1)

    exponents = []
    for i in pf:
        exponents.append(int((q-1)/i))
    
    r = 1
    while (r <= len(pf)):
        squared_pol = f
        for j in range(exponents[r-1] - 1):
            squared_pol = multiplication(squared_pol, squared_pol, m, h)
        if (squared_pol[0] == 1) and (len(squared_pol) == 1):
            break
        r += 1
        squared_pol.clear()

    if (r <= len(pf)):
        return False
    else:
        return True

