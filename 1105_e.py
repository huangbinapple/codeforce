import time
import copy

def find_max_clique(remain, chosen, max_, index):
    # print(remain, chosen, max_)
    result = chosen
    if len(chosen) + len(remain) <= max_:
        # print('pruning...')
        return None
    if not remain:
        # print('trivial')
        return result
    while remain:
        new_chosen = remain.pop()
        sub_result = find_max_clique(remain & index[new_chosen], chosen ^ {new_chosen} , max_, index)
        if sub_result and len(sub_result) > max_:
            max_ = len(sub_result)
            result = sub_result
    # print('result:', result)
    return result

def test_find():
    index = {1: {2, 3, 4}, 2: {1, 3, 4}, 3: {1, 2}, 4: {1, 2}}
    print(find_max_clique({1, 2, 3, 4}, set(), 0, index))

def solve(events):
    index = {}
    r = set()
    while events:
        ele = events.pop()
        if not ele:
            # ele is None
            r.clear()
        elif ele:
            # ele not None.
            if ele not in index:
                index[ele] = set()
            for n in r:
                index[n].add(ele)
            index[ele].update(r)
            r.add(ele)
    whole = set(index.keys())
    # print('w:', whole)
    for k in index.keys():
        index[k] = whole - index[k] - {k}
    return find_max_clique(whole, set(), 0, index)

def test():
    events = []
    for i in range(1, 11):
        events.extend([None, i])
    tick = time.time()
    print(solve(events))
    tock = time.time()
    print('T:', round(tock - tick, 5)) 
    
def main():
    # Deal input here.
    n, m = map(int, input().split())
    events = []
    d = {}
    id_ = 1
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
    print(len(solve(events)))
    # tock = time.time()
    # print(round(tock - tick, 5))


if __name__ == '__main__':
    main()
