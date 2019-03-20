import math
# import time
from copy import deepcopy


def matrix_dot(A, B):
    # print('enter dot')
    size_a = len(A), len(A[0])
    size_b = len(B), len(B[0])
    # print(size_a, size_b)
    assert size_a[1] == size_b[0]
    result = [[None for i in range(size_b[1])]
        for j in range(size_a[0])]
    for i in range(size_a[0]):
        for j in range(size_b[1]):
            result[i][j] = sum((A[i][k] * B[k][j] for
                k in range(size_a[1]))) % (10 ** 9 + 7)
    # print('exit dot')
    return result

def unit_matrix(m):
    result = [[0 for i in range(m)] for j in range(m)]
    for i in range(m):
        result[i][i] = 1
    return result

def matrix_power(A, pow):
    pows = []
    result = unit_matrix(len(A))
    while pow:
        last_digit, pow = pow % 2, pow // 2
        if not pows:
            pows.append(deepcopy(A))
        else:
            pows.append(matrix_dot(pows[-1], pows[-1]))
        # print('pow:', pow)
        if last_digit:
            result = matrix_dot(result, pows[-1])
        # print('haha')
    return result

def solve(n, l, r):
    a, b = (r - l + 1) // 3, (r - l + 1) % 3
    c = l % 3
    array = [a] * 3
    for i in range(b):
        array[(c + i) % 3] += 1
    
    # print('array:', array)

    matrix = [[array[0], array[2], array[1]],
        [array[1], array[0], array[2]],
        [array[2], array[1], array[0]]]
    array = [[ele] for ele in array]
    result = matrix_dot(matrix_power(matrix, n - 1), array)[0][0]
    # print('haha')
    return  result % (10 ** 9 + 7)
    
def main():
    n, l, r = map(int, input().split())
    # tick = time.time()
    print(solve(n, l, r))
    # tock = time.time()
    # print(round(tock - tick, 5))


if __name__ == '__main__':
    main()
