import copy

def helper(n):
    primes = []
    result = [{}]
    if n == 1:
        return result, primes
    for i in range(1, n + 1):
        for prime in primes:
            if i % prime == 0:
                new_result = copy.copy(result[i // prime - 1])
                if prime in new_result:
                    new_result[prime] += 1
                else:
                    new_result[prime] = 1
                result.append(new_result)
                break
            primes.append(i)
            result.append({i: 1})
    return result, primes

def test_helper():
    result, primes = helper(20)
    print('primes:', primes)
    for i, ele in enumerate(result, 1):
        print(i, ele)

def solve(n, m):
    pass
def main():
    n, m = map(int, input().split())
    print(solve(n, m))

if __name__ == "__main__":
    test_helper()