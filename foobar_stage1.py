def add(n1, n2, base):
    str_n1 = n1[::-1]
    str_n2 = n2[::-1]
    num1 = num2 = 0

    for i in range(0, len(str_n1)):
        num1 += int(str_n1[i]) * (base ** i)
        num2 += int(str_n2[i]) * (base ** i)

    num3 = num1 - num2
    str_n3 = ''

    while num3 != 0:
        str_n3 += str(num3 % base)
        num3 = num3 // base

    if len(str_n3) != len(n1):
        str_n3 += '0' * (len(n1) - len(str_n3))

    return str_n3[::-1]


def solution(n, b):
    cycle_arr = []
    next_num = n
    while next_num not in cycle_arr:
        assending = ''.join(sorted(next_num))
        dessending = ''.join(sorted(next_num, reverse=True))
        cycle_arr.append(next_num)
        next_num = add(dessending, assending, b)
    return len(cycle_arr) - cycle_arr.index(next_num)


print(solution('210022', 3))


