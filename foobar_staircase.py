def solution(n):
    pass

# The actual solutions
def parition(n):
    table = [[0 for i in range(n + 1)] for i in range(n + 1)]
    table[0][0] = 1

    for row in range(1, len(table)):
        for col in range(len(table[0])):
            if col < row:
                table[row][col] = table[row - 1][col]
            else:
                table[row][col] = table[row - 1][col] + table[row - 1][col - row]
    return table[-1][-1] - 1


def pretty(table):
    for row in table:
        print(row)

print(parition(200))

# My previous attempts
'''
sums = [[{0}], [{0, 1}], [{0, 2}], [{0, 3}, {0, 1, 2}]]

def look_up(n):
    possible_sums = []
    for i in range(1, n // 2 + 1):
        tmp_sum = {i}
        existing_sub_sums = sums[n - i]
        for sum1 in existing_sub_sums:
            if sum(sum1.union(tmp_sum)) == n:
                possible_sums.append(sum1.union(tmp_sum))
    return possible_sums

def gen(n):
    for i in range(4, n + 1):
        sums.append([{0, i}])
        tmp_ls = look_up(i)
        sums[i].extend(list(tmp_ls))
'''
'''

N = 30
numbers = [i for i in range(1, N)]
count = 0

def sum_checker(partial, n):
    global count
    partial_sum = partial[0]
    needed_num = n - partial_sum
    if needed_num > partial[0] and needed_num < n:
        count += 1
        for i in range(1, len(partial)):
            partial_sum += partial[i]
            needed_num = n - partial_sum
            if needed_num > partial[i] and needed_num < n:
                count += 1
                for j in range(i + 1, len(partial)):
                    partial_sum += partial[j]
                    needed_num = n - partial_sum
                    if needed_num > partial[j]:
                        count += 1
                    else:
                        partial_sum = partial[0]
                        break
            else:
                break
        sum_checker(partial[1:], n)

    return True

sum_checker(numbers, N)
print(count)
'''