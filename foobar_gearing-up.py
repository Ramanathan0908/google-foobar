''''
def last_gear(first_gear, diference):
    gear_ratios = []
    last_gear = first_gear
    for diff in diference:
        last_gear = diff - last_gear
        gear_ratios.append(last_gear)
    return last_gear


def solution(pegs):
    diff = []
    for i in range(len(pegs) -1):
        diff.append(pegs[i + 1] - pegs[i])
    for i in range(1, diff[0]):
        if i == 2 * last_gear(i, diff):
            return [i, 1]
    return [-1, -1]

print(solution([4, 30, 50]))
'''
def new_gear(diff, prev_expression):
    return (diff - prev_expression[0], -1 * prev_expression[1])

def solution(pegs):
    diff = []
    for i in range(len(pegs) -1):
        diff.append(pegs[i + 1] - pegs[i])
    last_gear = (0, 1)
    gears = []
    for dif in diff:
        last_gear = new_gear(dif, last_gear)
        gears.append(last_gear)

    i, j = last_gear
    i = 2 * i
    j = -1 * (2 * j - 1)
    
    for gear in gears:
        if gear[0] + gear[1] * (i / j) <= 0:
            return [-1, -1]

    if i / j <= 1 or (i / j) >= diff[0]:
        return [-1, -1]
    
    if j == -1 and i < 0 and (i / j) < diff[0]:
        return [-1 * i, 1]
    
    if j == 3 and i > 4 and (i / j) < diff[0]:
        if i % 3 == 0:
            return[int(i / 3), 1]
        if i % 3 == 1 or i % 3 == 2:
            return [i, 3]
    return [-1, -1]

print(solution([4, 30, 50]))