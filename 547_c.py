# import time

def solve(n, deltas):
    min_ = 1
    l = [1]
    for ele in deltas:
        new = l[-1] + ele
        min_ = min(min_, new)
        l.append(new)
    l_s = sorted(l)
    for i, ele in enumerate(l_s):
        if i != ele - min_:
            return '-1'
    return ' '.join(map(str, [ele - min_ + 1 for ele in l]))

def main():
    n = int(input())
    deltas = list(map(int, input().split()))
    # tick = time.time()
    print(solve(n, deltas))
    # tock = time.time()
    # print('T:', round(tock - tick, 5))

if __name__ == "__main__":
    main()