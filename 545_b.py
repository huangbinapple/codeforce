# import time
import random


def helper(s):
    size = len(s)
    c_l, c_r = [0, 0], [0, 0]
    candidate_overlaps = []
    for i in range(size):
        if s[i] == '0':
            c_l[0] += 1
        else:
            c_l[1] += 1
        if s[size - 1 - i] == '0':
            c_r[0] += 1
        else:
            c_r[1] += 1
        if c_l == c_r:
            candidate_overlaps.append(i + 1)
    # Get ride of the trivial overlap size, with is the length of s.
    candidate_overlaps.pop()
    result = 0
    # print('candidates:', candidate_overlaps)
    for overlap in reversed(candidate_overlaps):
        # print('overlap:', overlap)
        delta = size - overlap
        # print('delta:', delta)
        found = True
        for start in range(overlap):
            if s[start] != s[start + delta]:
                found = False
                break
        if found:
            result = overlap
            break
    return result

def counter(s):
    a, b = 0, 0
    for ele in s:
        if ele == '0':
            a += 1
        else:
            b += 1
    return a, b

def test_helper():
    i = [''.join(('1' if random.random() > .05 else '0' for i in range(500000)))]
    i = ['1'] * 500000
    i[-2] = '0'
    i = [''.join(i)]
    i = ['101', '110']
    print('haha')
    for ele in i:
        print(helper(ele))

def solve(s, t):
    s_0, s_1 = counter(s)
    m = helper(t)
    t_repeat = t[:m]
    t_remain = t[m:]
    t_repeat_0, t_repeat_1 = counter(t_repeat)
    t_remain_0, t_remain_1 = counter(t_remain)
    if t_repeat_0 > s_0 or t_repeat_1 > s_1:
        return s
    result = []
    s_0 -= t_repeat_0
    s_1 -= t_repeat_1
    result.append(t_repeat)
    if t_remain_0 == 0:
        n = s_1 // t_remain_1
    elif t_remain_1 == 0:
        n = s_0 // t_remain_0
    else:
        n = min(s_0 // t_remain_0, s_1 // t_remain_1)
    s_0 -= n * t_remain_0
    s_1 -= n * t_remain_1
    result.append(t_remain * n)
    result.append('0' * s_0)
    result.append('1' * s_1)

    return ''.join(result)
            
def main():
    # Deal with input.
    s = input()
    t = input()
    # tick = time.time()
    result = solve(s, t)
    # tock = time.time()
    # Deal with output.
    print(result)

    # Printe time.
    # print('T:', round(tock - tick ,5))

def test():
    pass

if __name__ == "__main__":
    main()