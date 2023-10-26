def next_power_of_2(n):
    # Find the smallest power of 2 that's greater than or equal to n
    power = 1
    while power < n:
        power *= 2
    return power

def remove_leading_zeros(lst):
    # Remove leading zeros from a list
    while lst and lst[-1] == 0:
        lst.pop()
    return lst

def polynomial_multiplication(f, g, p):

    if not f or not g:
        return [0]

    n = max(len(f), len(g))
    n = next_power_of_2(n)  # Pad to the next power of 2
    
    # Pad with zeros to make lengths equal and a power of 2
    while len(f) < n:
        f.append(0)
    while len(g) < n:
        g.append(0)
    
    # Base case: If the polynomial is of degree 0 or 1
    if n == 1:
        return [(f[0] * g[0]) % p]
    
    # Split the polynomials into two halves
    mid = n // 2
    f0, f1 = f[:mid], f[mid:]
    g0, g1 = g[:mid], g[mid:]
    
    # Recursive multiplication
    f0g0 = polynomial_multiplication(f0, g0, p)
    f1g1 = polynomial_multiplication(f1, g1, p)
    f0_plus_f1 = [(a + b) % p for a, b in zip(f0, f1)]
    g0_plus_g1 = [(a + b) % p for a, b in zip(g0, g1)]
    middle_term = polynomial_multiplication(f0_plus_f1, g0_plus_g1, p)
    
    # Correctly compute the middle term considering possible different lengths
    for i in range(len(middle_term)):
        if i < len(f0g0):
            middle_term[i] -= f0g0[i]
        if i < len(f1g1):
            middle_term[i] -= f1g1[i]
        middle_term[i] %= p
    
    # Combine the results
    result = [0] * (2 * n - 1)
    for i in range(len(f0g0)):
        result[i] += f0g0[i]
    for i in range(len(middle_term)):
        result[i + mid] += middle_term[i]
    for i in range(len(f1g1)):
        result[i + 2 * mid] += f1g1[i]
    
    # Remove leading zeros
    result = remove_leading_zeros(result)
    
    return [x % p for x in result]

# # 1. Basic Cases
# f = [1, 2, 3]
# g = [4, 5]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == [4, 13, 22, 15]

# f = [1]
# g = [1]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == [1]

# # 2. Zero Cases
# f = [0, 0, 0]
# g = [0, 0, 0]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == []

# f = [1, 2, 3]
# g = [0, 0]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == []

# # 3. Large Number Cases
# f = [987654321]
# g = [123456789]
# p = 1000000007
# answer = 987654321 * 123456789 % p  
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == [answer]

# f = [999999999, 888888888]
# g = [777777777, 666666666]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == [999999999 * 777777777 % p, (777777777 * 888888888 % p + 999999999 * 666666666 % p) % p, 888888888 * 666666666 % p]

# # 4. Edge Cases
# f = [1, 2, 3, 4]
# g = [5, 6, 7, 8]
# p = 1000000007
# assert polynomial_multiplication(f, g, p) == [5, 16, 34, 60, 61, 52, 32]

# f = []
# g = []
# p = 1000000007
# print(polynomial_multiplication(f, g, p))
# assert polynomial_multiplication(f, g, p) == [0]

# print("All tests passed!")
