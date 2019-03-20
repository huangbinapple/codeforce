# import time
import copy

def helper(m):
    n_2, n_3 = 0, 0
    while m % 2 == 0:
        m //= 2
        n_2 += 1
    while m % 3 == 0:
        m //= 3
        n_3 += 1
    return n_2, n_3, m

def test_helper():
    result, primes = helper(20)
    print('primes:', primes)
    for i, ele in enumerate(result, 1):
        print(i, ele)

def solve(n, m):
    n_2, n_3, n_r = helper(n)
    m_2, m_3, m_r = helper(m)
    if m_r == n_r and m_2 >= n_2 and m_3 >= n_3:
        return m_2 + m_3 - n_2 - n_3
    else:
        return -1

def main():
    n, m = map(int, input().split())
    # tick = time.time()
    print(solve(n, m))
    # tock = time.time()
    # print('T: {}'.format(round(tock - tick, 5)))

if __name__ == "__main__":
    main()