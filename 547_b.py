# import time

def solve(n, flags):
    result = 0
    k = 0
    sub_result = 0
    first_time = True
    for ele in flags:
        if ele == 1:
            sub_result += 1
        else:
            result = max(result, sub_result)
            sub_result = 0
            if first_time:
                k = result
            first_time = False
    if ele == 1:
        result = max(result, sub_result + k)
    # print(k)
    return result

def main():
    n = int(input())
    flags = list(map(int, input().split()))
    # tick = time.time()
    print(solve(n, flags))
    # tock = time.time()
    # print('T:', round(tock - tick, 5))

if __name__ == "__main__":
    main()