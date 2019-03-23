import time

def find_max_clique(remain, size, max_, index, maxs):
    result = max_
    if size + len(remain) <= result:
        return result
    if not remain:
        return size
    while remain:
        candidate = max(remain)
        if maxs[candidate] + size <= result:
            return result
        if size + len(remain) <= result:
            return result
        remain.remove(candidate)
        sub_result = find_max_clique(remain & index[candidate], size + 1 , result, index, maxs)
        if sub_result > result:
            result = sub_result
            return result
    return result

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
    for i in range(m):
        index[i] = whole - index[i] - {i}
    maxs = [0] * m
    whole = set()
    for i in range(m):
        whole.add(i)
        maxs[i] = max(maxs[i - 1], find_max_clique(whole & index[i], 1, maxs[i - 1], index, maxs))
    return maxs[-1]
    
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
    print(solve(events, m))


if __name__ == '__main__':
    main()
