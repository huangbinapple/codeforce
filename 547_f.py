import time
def index(key, item, index):
    if key in index:
        index[key].add(item)
    else:
        index[key] = set([item])

def schedule_(times, n):
    d = [None] * (n + 1)
    for start, end in times:
        for i in range(start + 1):
            if d[i] is None or end < d[i][1]:
                d[i] = (start, end)
    # print('d:', d)
    result = []
    next_ = d[0]
    while next_:
        result.append(next_)
        s = next_[1]
        next_ = d[s]
    return result

def schedule(times):
    # print('\nin schedule')
    index_by_a = {}
    index_by_b = {}
    result_indexs = []
    for i in range(len(times)):
        a, b = times[i]
        index(a, i, index_by_a)
        index(b, i, index_by_b)
    b_keys = sorted(list(index_by_b.keys()))
    # a_keys = sorted(list(index_by_a.keys()))
    
    result = []
    a_min = 0
    # Get interval with minimun end time whose start time >= a_min.
    flag = True
    while flag:
        flag = False
        for end_time in (ele for ele in b_keys if ele > a_min):
            for start in (times[i][0] for i in index_by_b[end_time]):
                if start >= a_min:
                    flag = True
                    result.append((start, end_time)) 
                    a_min = end_time
                    break
            if flag:
                break
    return result
                
def test_schedule():
    i = ((0, 4), (2, 4), (0, 2), (0, 1), (1, 2), (2, 3), (3, 4))
    result = schedule(i)
    print('len:', len(result))
    for ele in result:
        print(ele)

def solve(n, a_l):
    index_by_sum = {}
    for i in range(n):
        sum_ = 0
        for j in range(i + 1, n + 1):
            sum_ += a_l[j - 1]
            if sum_ in index_by_sum:
                index_by_sum[sum_].append((i, j))
            else:
                index_by_sum[sum_] = [(i, j)]
    print('haha')
    result = []
    for sum_, times in index_by_sum.items():
        # print('Finished sum:', sum_)
        sub_result = schedule(times)
        if len(sub_result) > len(result):
            result = sub_result
    return result

def main():
    # n = int(input())
    # a_l = list(map(int, input().split()))
    n = 1500
    a_l = range(1, n + 1)
    tick = time.time()
    result = solve(n, a_l)
    print(len(result))
    for a, b in result:
        print(a + 1, b)
    tock = time.time()
    print('T:', round(tock - tick, 5))

if __name__ == "__main__":
    main()