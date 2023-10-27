
# Polynomial Addition
# Input: Two polynomials f and g in F[x] represented as arrays of coefficients
#        and a modulus m
# Output: A polynomial representing f + g under the given modulus m
# Example:
# f = [2, 1, 1]
# g = [1, 1]
# p = 3
def polynomial_addition(f, g, m):
    answer = []
    maximum = max(len(f), len(g)) 
    minimum = min(len(f), len(g)) 

    #appending 0s to answer list based on polynomial size to index it later
    for i in range(maximum): 
        if (i < minimum): 
            answer.append((f[i] + g[i]) % m)
        #if the degree of f is greater than g, append the remaining coefficients of f    
        else: 
            if (len(f) > len(g)):
                answer.append(f[i])
            else:
                answer.append(g[i])
    return answer


# Test 1
# first = [2, 1, 1]
# second = [1, 1]
# p = 3
# print(polynomial_addition(first, second, p))

