from polynomial_addition import polynomial_addition
from polynomial_multiplication import polynomial_multiplication
from polynomial_subtraction import polynomial_subtraction


def remove_leading_zeros(f):
    for i in range(len(f)):
        if f[-1] == 0 and f.count(f[0]) != len(f):
            del f[-1]
        else:
            break


    q = []
    r = f.copy()

    while len(r) >= len(g):
        # Calculate the factor to make the leading coefficient of r match the leading coefficient of g
        term_mul_factor = r[-1] * pow(g[-1], -1, p)
        term_mul_position = len(r) - len(g)

        intermediate = [0] * (term_mul_position + 1)
        intermediate[term_mul_position] = term_mul_factor
        q = polynomial_addition(q, intermediate, p)

        subtracted = polynomial_multiplication(intermediate, g, p)
        r = polynomial_subtraction(r, subtracted, p)
        remove_leading_zeros(r)

        # If the remainder becomes the zero polynomial, break
        if not r:
            break

    return q, r

# Example usage:
# f = [1, 0]  # Represents 1X
# g = [1]    # Represents 1

# q, r = polynomial_long_division(f, g, 3)
# print("Quotient:", q)  # Expected: [1, 0]
# print("Remainder:", r) # Expected: []

# # # Example usage:
# # f = [1, 0, 2]  # Represents 1 + 2X^2
# # g = [1, 1]    # Represents 1 + X
# # p = 3

# # q, r = polynomial_long_division(f, g, p)
# # print("Quotient:", q)  # Expected: [2]
# # print("Remainder:", r) # Expected: [1]
