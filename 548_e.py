import time
import itertools

def dfs(p_to_c, start, used):
    size = len(p_to_c)
    used_copy = used.copy()
    # print('start:', start)
    max_, depth = 0, 0
    frontier = [ele for ele in p_to_c[start] if not used[ele]]
    # print('f:', frontier)
    while frontier:
        ele = frontier.pop()
        if type(ele) == tuple:
            used[ele[0]] = False
            depth -= 1
        else:
            frontier.append((ele,))
            used[ele] = True
            depth += 1
            if start + depth < size:
                new_nodes = [e for e in p_to_c[start + depth] if not used[e]]
            else:
                new_nodes = []
            # print('new_nodes:', new_nodes)
            frontier.extend(new_nodes)
            if not new_nodes:
                # print('ya')
                max_ = max(max_, depth)
                used_copy = used.copy()
    return (max_, used_copy)

def solve(potentials, clubs, dies, m, n, d):
    p_to_c = [set() for i in range(5000)]
    dies_ = set(dies)
    used = [False for i in range(m)]
    for i in filter(lambda x: x not in dies_, range(n)):
        potential = potentials[i]
        club = clubs[i]
        p_to_c[potential].add(club)
    mex, used = dfs(p_to_c, 0, used)
    result = [mex]
    # print(p_to_c)
    # print(used)
    while len(dies) > 1:
        # print()
        # Add new node.
        new = dies.pop()
        new_potential = potentials[new]
        new_club = clubs[new]
        # print('new:', new, new_potential, new_club)
        p_to_c[new_potential].add(new_club)
        # print(p_to_c)
        # print(used)
        # print('mex:', mex)
        if new_potential != mex:
            used = [False for i in range(m)]
            mex, used = dfs(p_to_c, 0, used)
        elif used[new_club]:
            # print('haha')
            used = [False for i in range(m)]
            mex, used = dfs(p_to_c, 0, used)
        else:
            # print('yoyo')
            mex_delta, used = dfs(p_to_c, mex, used)
            mex += mex_delta
        # print('mex:', mex)
        result.append(mex)
    return reversed(result)


def main():
    # Deal with input.
    n , m = map(int, input().split())
    potentials = list(map(int, input().split()))
    clubs = list(map(lambda x: int(x) - 1, input().split()))
    d = int(input())
    dies = []
    for _ in range(d):
        dies.append(int(input()) - 1)
    # tick = time.time()
    result = solve(potentials, clubs, dies, m, n, d)
    # tock = time.time()
    # Deal with output.
    for ele in result:
        print(ele)
    # Printe time.
    # print('T:', round(tock - tick ,5))

def test():
    n, m = 5000, 5000
    potentials = list(range(n))
    clubs = list(range(m))
    dies = list(reversed(range(1, n + 1)))
    d = n
    tick = time.time()
    result = solve(potentials, clubs, dies, m, n, d)
    tock = time.time()
    # Deal with output.
    for ele in result:
        print(ele)
    # Printe time.
    print('T:', round(tock - tick ,5))


if __name__ == "__main__":
    main()