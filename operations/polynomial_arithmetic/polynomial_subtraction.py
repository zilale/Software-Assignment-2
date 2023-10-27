#Function to subtract two polynomials f and g under the given modulus m

# Input: Two polynomials f and g, and a modulus m
# Output: A polynomial representing f - g under the given modulus m
# Example:
# f = [2, 1, 1]
# g = [1, 1]
# p = 3
# print(polynomial_subtraction(f, g, p))
def polynomial_subtraction(f, g, m):
    answer = []
    maximum = max(len(f), len(g)) 
    minimum = min(len(f), len(g)) 
        
    #appending 0s to answer list based on polynomial size to index it later    
    for i in range(maximum): 
        if (i < minimum): 
            answer.append((f[i] - g[i]) % m)
        else: 
            if (len(f) > len(g)): 
                answer.append(f[i])
            else:
                answer.append((-g[i]) % m) 
    return answer


# Test 1
# first = [2, 1]
# second = [1, 1]
# p = 3
# print(polynomial_addition(first, second, p))

