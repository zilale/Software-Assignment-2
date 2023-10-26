from polynomial_addition import polynomial_addition
from polynomial_multiplication import polynomial_multiplication
from polynomial_subtraction import polynomial_subtraction


def remove_leading_zeros(f):
    for i in range(len(f)):
        if f[-1] == 0 and f.count(f[0]) != len(f):
            del f[-1]
        else:
            break

def polynomial_long_division(f, g, p):
     #initializing the quotient
        q = [0]
        r = f.copy()

        # while the degree of r is greater than or equal to the degree of g
        while ((len(r) - 1) >= (len(g) - 1)):

            # add the quotient to the answer
            intermediate = [0] * (len(r) - len(g) + 1)    
            intermediate[len(r) - len(g)] = r[len(r) - 1] * pow(g[len(g) - 1], -1, p)

            q = polynomial_addition(q, intermediate,p)

            intermediateAdd = [0] * (len(r) - len(g) + 1)
            intermediateAdd[len(r) - len(g)] = (r[len(r) - 1] * pow(g[len(g) - 1], -1, p))

            # remainder is equal to the remainder minus the product of the quotient and the divisor
            r = polynomial_subtraction(r, polynomial_multiplication(intermediateAdd, g, p),p)

            del r[len(r) - 1]


        # remove leading zeros
        q[-1] = q[-1] % p
        remove_leading_zeros(q)
        remove_leading_zeros(r)
        return q, r

# Example usage:
f = [1, 0, 2]  # Represents 1 + 2X^2
g = [1, 1]    # Represents 1 + X
p = 3

q, r = polynomial_long_division(f, g, p)
print("Quotient:", q)  # Expected: [2]
print("Remainder:", r) # Expected: [1]
