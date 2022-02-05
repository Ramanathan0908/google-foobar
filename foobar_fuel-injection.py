def solution(n):
    num = int(n)
    if num <= 1:
        return 1

    if num % 2 == 0:
        count = 0
        while num != 1:
            if num % 2 == 0:
                num /= 2
                count += 1
            else:
                count += 2
                num = (num + 1) / 2
        return count

    count = 1
    num += 1
    while num != 1:
        if num % 2 == 0:
                num /= 2
                count += 1
        else:
            count += 2
            num = (num + 1) / 2
    return count

print(solution('42'))