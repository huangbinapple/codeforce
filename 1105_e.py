import time
import copy

def find_max_clique(root, index, pre_set, depth):
    # print('in find:', root, pre_set, depth)
    next_ = index[root] & pre_set
    result = depth
    for n in next_:
        result = max(result, find_max_clique(n, index, next_, depth + 1))
    return result

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
    for s in index.values():
        s.add(None)
    # Add fake node.
    index[None] = whole
    # for k, v in index.items():
        # print(k, v)
    result = find_max_clique(None, index, whole, depth=0)
    return result

def test():
    events = []
    for i in range(1, 20):
        events.extend([None, i])
    tick = time.time()
    print(solve(events))
    tock = time.time()
    print(round(tock - tick, 5)) 
    
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
    print(solve(events))
    # tock = time.time()
    # print(round(tock - tick, 5))


if __name__ == '__main__':
    test()
