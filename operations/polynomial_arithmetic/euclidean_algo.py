from polynomial_longdivision import polynomial_long_division

def extended_euclidean_algo(f, g, p):
    while g!=0:
        _, r = polynomial_long_division(f, g, p)
        f, g = g, r

        

    return 