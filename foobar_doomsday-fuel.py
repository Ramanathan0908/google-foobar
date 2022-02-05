from fractions import Fraction

def pretty_print(m):
    for row in m:
        print(row)

# returns an identity m of size n
def identity(n):
    identity = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                identity[i][j] = 1
    return identity

# returns the result of subtraction of first m with second m
def subtraction(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m2)):
            m1[i][j] = m1[i][j] - m2[i][j]
    return m1

# returns the result of multiplication of m1 & m2
def multiplication(m1, m2):
    m2 = adjugate(m2)
    result = []
    for row in m1:
        arr = []
        for row2 in m2:
            sum = 0
            for i in range(len(row)):
                sum += row[i] * row2[i]
            arr.append(sum)
        result.append(arr)
    return result

# transposes the matrix
def adjugate(m):
    return list(map(list, zip(*m)))

# returns the minor for a given element in the matrix, i.e the matrix without the elemetns row and column
def matrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in m[:i] + m[i+1:]]

# calculates the determinant of a given matrix
def determinant(m):
    # use 2x2 matrices as base case, computate then return the determinant
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]

    det, power = 0, 1

    for i in range(len(m)):
        det += power * m[0][i] * determinant(matrixMinor(m, 0, i))
        power *= -1

    return det

# returns the respective minors for any given elements 
def matrix_of_minors(m):
    return [[determinant(matrixMinor(m, i, j)) for j in range(len(m))] for i in range(len(m))]

# returns the cofactors of the given matrix
def matrix_of_cofactors(m):
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if (i + j) % 2 == 1:
                m[i][j] *= -1
    return m

# returns the inverse of a given matrix 
def inverse(m):
    det = Fraction(1, determinant(m))
    if len(m) == 2:
        return [[m[1][1] * det, -1 * m[0][1] * det], [-1 * m[1][0] * det, m[0][0] * det]]
    inverse_m = adjugate(matrix_of_cofactors(matrix_of_minors(m)))
    for i in range(len(inverse_m)):
        for j in range(len(inverse_m)):
            inverse_m[i][j] *= det
    return inverse_m

# splits the input matrix into Q & R needed for absorbing markov chains and also turn the trails into probability
def foobar_matrix(m):
    terminal_states = [False for i in range(len(m))]
    no_of_terminal = 0
    for i , state in enumerate(m):
        if sum(state) == 0:
            terminal_states[i] = True
            no_of_terminal += 1
    if terminal_states[0]:
        return no_of_terminal, None
    standard_markov = [row for i, row in enumerate(m) if terminal_states[i]] + [row for i, row in enumerate(m) if not terminal_states[i]]
    R, Q = [], []
    for i in range(no_of_terminal, len(m)):
        denom = sum(standard_markov[i])
        R.append([Fraction(standard_markov[i][j], denom) for j in range(len(m)) if terminal_states[j]])
        Q.append([Fraction(standard_markov[i][j], denom) for j in range(len(m)) if not terminal_states[j]])
    return R, Q

# returns the lcm of given numbers in the input array
def lcm(arr):
    biggest = max(arr)
    for i in arr:
        while biggest % i != 0:
            biggest += 1
    return biggest

# returns the resultant matrix according to requirements from the input array
def solution(m):
    if len(m) < 2:
        return [1, 1]
    R, Q = foobar_matrix(m)
    if Q == None:
        return [1] + [0 for i in range(R - 1)] + [1]
    elif sum(sum(i) for i in Q) == 0:
        denom = max(i.denominator for i in R[0])
        return [(i * denom).numerator for i in R[0]] + [denom]
    F = inverse(subtraction(identity(len(Q)), Q))
    FR = multiplication(F, R)
    LCM = lcm([i.denominator for i in FR[0]])
    return [(i * LCM).numerator for i in FR[0]] + [LCM]

sample = [
  [0,1,4,5,6,7],  # s0, the initial state, goes to s1 and s5 with equal probability
  [0,0,0,0,0,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,3,4,1,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,4,5,6,1],  # s4 is terminal
  [0,0,2,0,4,0],  # s5 is terminal
]

sample2 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]

sample3 = [
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

print(solution(sample3))
