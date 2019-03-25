import time


def schedule2(times):
    result = []
    a_min = 0
    for s, e in times:
        if s >= a_min:
            result.append((s, e))
            a_min = e
    return result

def solve(n, a_l):
    index_by_sum = {}
    for j in range(1, n + 1):
        sum_ = 0
        for i in range(j - 1, -1, -1):
            sum_ += a_l[i]
            if sum_ in index_by_sum:
                index_by_sum[sum_].append((i, j))
            else:
                index_by_sum[sum_] = [(i, j)]
    result = []
    for sum_, times in index_by_sum.items():
        sub_result = schedule2(times)
        if len(sub_result) > len(result):
            result = sub_result
    return result

def test():
    n = 1500
    a_l = list(range(1, n + 1))
    tick = time.time()
    result = solve(n, a_l)
    tock = time.time()
    print(len(result))
    for a, b in result:
        print(a + 1, b)
    print("T:", round(tock - tick, 5))


def main():
    n = int(input())
    a_l = list(map(int, input().split()))
    result = solve(n, a_l)
    print(len(result))
    for a, b in result:
        print(a + 1, b)

if __name__ == "__main__":
    main()