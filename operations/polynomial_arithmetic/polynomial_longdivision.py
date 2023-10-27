from operations.polynomial_arithmetic.polynomial_addition import polynomial_addition
from operations.polynomial_arithmetic.polynomial_multiplication import polynomial_multiplication
from operations.polynomial_arithmetic.polynomial_subtraction import polynomial_subtraction

def remove_leading_zeros(f):
    help = 0
    reversed = reversed(f)
    for i in reversed:
        if i != 0:
            if help > 0:   return f[:-help]
            else:       return f
        help += 1
    return [0]

#Function to divide two polynomials f and g under the given modulus m
def polynomial_long_division(a, b, m):
    q = [0]
    r = a
    while ((len(r) - 1) >= (len(b) - 1)):
        intermediate = []
        for i in range(len(r) - len(b) + 1):
            intermediate.append(0)
        intermediate[len(r) - len(b)] = r[len(r) - 1] * pow(b[len(b) - 1], -1, m)
        q = polynomial_addition(q, intermediate, m)
        secondIntermediate = []

        for i in range(len(r) - len(b) + 1):
            secondIntermediate.append(0)
        secondIntermediate[len(r) - len(b)] = (r[len(r) - 1] * pow(b[len(b) - 1], -1, m))
        r = polynomial_subtraction(r, polynomial_multiplication(secondIntermediate, b, m), m)
        #removing any leading zeroes
        del r[len(r) - 1]
    q[-1] = q[-1]%m

    return remove_leading_zeros(q), remove_leading_zeros(r)

