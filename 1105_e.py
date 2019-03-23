import time

def find_max_clique(remain, size, max_, index):
    # print(remain, chosen, max_)
    result = max_
    if size + len(remain) <= result:
        # print('pruning...')
        return result
    if not remain:
        # print('trivial')
        return size
    while len(remain) + size > result:
        candidate = remain.pop()
        sub_result = find_max_clique(remain & index[candidate], size + 1 , result, index)
        result = max(result, sub_result)
    # print('result:', result)
    return result

def test_find():
    index = {1: {2, 3, 4}, 2: {1, 3, 4}, 3: {1, 2}, 4: {1, 2}}
    print(find_max_clique({1, 2, 3, 4}, 0, 0, index))

def solve(events, m):
    index = [set() for _ in range(m)]
    r = []
    while events:
        ele = events.pop()
        if ele is None:
            # ele is None
            r.clear()
        else:
            # ele not None.
            for n in r:
                index[n].add(ele)
            index[ele].update(r)
            r.append(ele)
    whole = set(range(m))
    # print('w:', whole)
    for i in range(m):
        index[i] = whole - index[i] - {i}
    return find_max_clique(whole, 0, 0, index)

def test():
    events = []
    for i in range(500):
        events.extend([None, i])
    tick = time.time()
    print(solve(events, 500))
    tock = time.time()
    print('T:', round(tock - tick, 5)) 
    
def main():
    # Deal input here.
    n, m = map(int, input().split())
    events = []
    d = {}
    id_ = 0
    for i in range(n):
        line = input()
        if line.startswith('1'):
            events.append(None)
        else:
            if line not in d:
                d[line] = id_
                id_ += 1
            events.append(d[line])
    
    # tick = time.time()
    print(solve(events, m))
    # tock = time.time()
    # print(round(tock - tick, 5))


if __name__ == '__main__':
    main()
