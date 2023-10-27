import random

from operations.finite_fields_arithmetic.primitivity_check import primitivity_checking

def primitive_element_generation(m, h):
        poly = []

        for i in range(len(h)-1):
            poly.append(random.randint(0,m-1)%m)

        while primitivity_checking(poly, m, h) == False:
            poly = []
            for i in range(len(h)-1):
                poly.append(random.randint(0,m-1)%m)

        remove_leading_zeros(poly)
        return poly


def remove_leading_zeros(f):
    help = 0
    takel = reversed(f)
    for i in takel:
        if i != 0:
            if help > 0:   return f[:-help]
            else:       return f
        help += 1
    return [0]
