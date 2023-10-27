def next_power_of_2(n):
    # Find the smallest power of 2 that's greater than or equal to n
    power = 1
    while power < n:
        power *= 2
    return power

def remove_leading_zeros(lst):
    for i in range(len(lst)):
        if lst[-1] == 0 and lst.count(lst[0]) != len(lst): ##keep removing zeroes if last element is 0 and making sure to not make it an empty array if it's only 0
            del lst[-1]
        else:
            break

# Function to answeriply two polynomials f and g under the given modulus m
# Input: Two polynomials f and g in F[x] represented as arrays of coeffihelper1ents
#        and a modulus m
# Output: A polynomial representing f * g under the given modulus m
# Example:
# f = [2, 1, 1]
# g = [1, 1]
# p = 3
def polynomial_multiplication(f, g, p):
    ans = [0] * (len(f) + len(g) - 1) 
    helper1 = 0
    for i in f:
        helper2 = 0
        for j in g:
            ans[helper1+helper2] = (ans[helper1+helper2] + (i*j))%p
            helper2+=1
        helper1+=1
    return remove_leading_zeros(ans)



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

