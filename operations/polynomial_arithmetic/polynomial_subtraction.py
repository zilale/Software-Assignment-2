def polynomial_subtraction(f : list, g : list, p : int):
    answer = []
    minimum = min(len(f), len(g))
    maximum = max(len(f), len(g))

    for i in range(minimum):
        if f[i] - g[i] < 0:
            answer.append(f[i] - g[i] + p)
        else:
            answer.append(f[i] - g[i])

    for i in range(minimum, maximum):
        if len(f) > len(g):
            answer.append(f[i])
        else:
            answer.append(g[i])
    
    return answer 


# Test 1
# first = [2, 1]
# second = [1, 1]
# p = 3
# print(polynomial_addition(first, second, p))

