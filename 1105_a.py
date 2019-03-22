def solve(n, lengths):
    counters = [0] * 100
    for l in lengths:
        counters[l - 1] += 1
    ptr_l = -1
    ptr_r = 100
    c_l, c_r = 0, 0
    while ptr_r - ptr_l > 2:
        if c_l <= c_r:
            ptr_l += 1
            c_l += counters[ptr_l]
        else:
            ptr_r -= 1
            c_r += counters[ptr_r]
    # print(ptr_l, ptr_r)
    center_index = ptr_l + 1
    center_length = center_index + 1
    cost = sum((ptr_l - i) * counters[i] for i in range(ptr_l)) + \
        sum((i - ptr_r) * counters[i] for i in range(ptr_r + 1, 100))
    return center_length, cost

def main():
    n = int(input())
    lengths = list(map(int, input().split()))
    result = solve(n, lengths)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()