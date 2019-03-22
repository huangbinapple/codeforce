def solve(s, k):
    counters = [0] * 26
    counter = 0
    state = None
    for ele in s:
        if ele != state:
            state = ele
            counter = 1
        else:
            counter += 1
        if counter == k:
            counters[ord(ele) - ord('a')] += 1
            counter = 0
    return max(counters)

def main():
    n, k = map(int, input().split())
    s = input()
    print(solve(s, k))

if __name__ == "__main__":
    main()