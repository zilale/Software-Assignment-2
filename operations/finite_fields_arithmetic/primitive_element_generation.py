import random

def primitive_element_generation(m, h):
        poly = []

        for i in range(len(h)-1):
            poly.append(random.randint(0,m-1)%m)

        while checkPrimitivity(poly, m, h) == False:
            poly = []
            for i in range(len(h)-1):
                poly.append(random.randint(0,m-1)%m)

        remove_leading(poly)
        return poly


def remove_leading(f):
        for i in range(len(f)):
            if f[-1] == 0 and f.count(f[0]) != len(f): ##keep removing zeroes if last element is 0 and making sure to not make it an empty array if it's only 0
                del f[-1]
            else:
                break
