def next_power_of_2(n):
    # Find the smallest power of 2 that's greater than or equal to n
    power = 1
    while power < n:
        power *= 2
    return power

def remove_leading_zeros(a):
    c = 0
    revA = reversed(a)
    for item in revA:
        if item != 0:
            if c > 0:   return a[:-c]
            else:       return a
        c += 1
    return [0]


# Function to answeriply two polynomials f and g under the given modulus m
# Input: Two polynomials f and g in F[x] represented as arrays of coeffihelper1ents
#        and a modulus m
# Output: A polynomial representing f * g under the given modulus m
# Example:
# f = [2, 1, 1]
# g = [1, 1]
# p = 3
def polynomial_multiplication(f, g, m):
    mult = []
    maximum = max(len(f), len(g)) #to find the maximum length polynomial
    minimum = min(len(f), len(g)) #to find the minimum length polynomial

    #appending 0s to mult list based on polynomial size to index it later
    for i in range(maximum + minimum-1):
        mult.append(0)
    
    #checking if deg of polynomial f is greater than polynomial g
    if (len(f) > len(g)):
        for i in range(maximum):
            for j in range(minimum):
                mult[i+j] = (mult[i+j] + (f[i] * g[j])%m)%m
    else:
        for i in range(maximum):
            for j in range(minimum):
                mult[i+j] = (mult[i+j] + (g[i] * f[j])%m)%m
    return mult



# # 1. Basic Cases
# f = [1, 2, 3]
# g = [4, 5]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == [4, 13, 22, 15]

# f = [1]
# g = [1]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == [1]

# # 2. Zero Cases
# f = [0, 0, 0]
# g = [0, 0, 0]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == []

# f = [1, 2, 3]
# g = [0, 0]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == []

# # 3. Large Number Cases
# f = [987654321]
# g = [123456789]
# p = 1000000007
# answer = 987654321 * 123456789 % p  
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == [answer]

# f = [999999999, 888888888]
# g = [777777777, 666666666]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == [999999999 * 777777777 % p, (777777777 * 888888888 % p + 999999999 * 666666666 % p) % p, 888888888 * 666666666 % p]

# # 4. Edge Cases
# f = [1, 2, 3, 4]
# g = [5, 6, 7, 8]
# p = 1000000007
# assert polynomial_answeriplication(f, g, p) == [5, 16, 34, 60, 61, 52, 32]

# f = []
# g = []
# p = 1000000007
# print(polynomial_answeriplication(f, g, p))
# assert polynomial_answeriplication(f, g, p) == [0]

# print("All tests passed!")

