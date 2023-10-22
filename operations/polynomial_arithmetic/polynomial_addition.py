def polynomial_addition(f : list, g : list, p : int):

    # define answer list
    answer = []
    minimum = min(len(f), len(g))
    maximum = max(len(f), len(g))

    # add elements of f and g to answer list
    # if sum of elements is greater than p, subtract p from sum
    for i in range(minimum):
        if g[i] + f[i] >= p:
            answer.append(g[i] + f[i] - p)
        else:
            answer.append(g[i] + f[i])

    # add remaining elements of f or g to answer list
    # if f or g is longer than the other, add remaining elements to answer list
    for i in range(minimum, maximum):
        if len(f) > len(g):
            answer.append(f[i])
        else:
            answer.append(g[i])
    
    return answer 


# Test 1
# first = [2, 1, 1]
# second = [1, 1]
# p = 3
# print(polynomial_addition(first, second, p))

