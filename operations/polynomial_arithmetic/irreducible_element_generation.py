from operations.polynomial_arithmetic.irreducibility_check import irreducibility_check
import random

def irreducible_element_generation(m,n):
    poly = []

    for i in range(n+1):
        poly.append(random.randint(0, m-1))

    while irreducibility_check(poly, m) == False:
        poly = []
        for i in range(n+1):
            poly.append(random.randint(0, m-1))
    return poly
