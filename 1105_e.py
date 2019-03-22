# import time


def solve(events, n, m):
    result = 0
    counter = {}
    while events:
        ele = events.pop()
        if not ele:
            result += max(counter.values())
            counter.clear()
        elif ele in counter:
            counter[ele] += 1
        else:
            counter[ele] = 1
    return result
    
def main():
    # Deal input here.
    n, m = map(int, input().split())
    events = []
    for i in range(n):
        line = input()
        events.append(None if line.startswith('1') else line[2:])
    
    # tick = time.time()
    print(solve(events, n, m))
    # tock = time.time()
    # print(round(tock - tick, 5))


if __name__ == '__main__':
    main()
