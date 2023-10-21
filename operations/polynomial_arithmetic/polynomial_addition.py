def polynomial_addition(f : list, g : list, p : int):
    answer = []
    carry = 0
    maximum = max(len(f), len(g))
    for i in range(maximum):
        if g[i] + f[i] + carry >= p:
            answer.append(g[i] + f[i] + carry - p)
            carry = 1
        else:
            carry = 0
            answer.append(g[i] + f[i] + carry)
    
    if carry == 1:
        answer.append(1)

    return answer 


# Test 1
# first = [2, 1]
# second = [1, 1]
# p = 3
# print(polynomial_addition(first, second, p))

