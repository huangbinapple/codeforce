import time


def get_frontiers(feild, n, m, p):
    frontiers = [[] for i in range(p)]
    for i in range(n):
        for j in range(m):
            ele = feild[i][j]
            if 1 <= ele <= 9:
                # print('ele:', ele)
                frontiers[ele - 1].append((i, j))
    return frontiers

def go(player_id, frontier, n_turn, feild, n, m):
    frontier = frontier
    while n_turn and frontier:
        n_turn -= 1
        new_frontier = []
        for i, j in frontier:
            # Down.
            if i + 1 < n:
                new_space = feild[i + 1][j]
                if not new_space:
                    feild[i + 1][j] = player_id
                    new_frontier.append((i + 1, j))
            # Up.
            if i - 1 >= 0:
                new_space = feild[i - 1][j]
                if not new_space:
                    feild[i - 1][j] = player_id
                    new_frontier.append((i - 1, j))
            # Rigth.
            if j + 1 < m:
                new_space = feild[i][j + 1]
                if not new_space:
                    feild[i][j + 1] = player_id
                    new_frontier.append((i, j + 1))
            # Left.
            if j - 1 >= 0:
                new_space = feild[i][j - 1]
                if not new_space:
                    feild[i][j - 1] = player_id
                    new_frontier.append((i, j - 1))
        frontier = new_frontier
    return frontier

def solve(speeds, feild, n, m, p):
    frontiers = get_frontiers(feild, n, m, p)
    hope = set(range(p))
    while hope:
        lost_hope = set()
        for i in hope:
            n_turn = speeds[i]
            frontier = frontiers[i]
            new_frontier = go(i + 1, frontier, n_turn, feild, n, m)
            if not new_frontier:
                lost_hope.add(i)
            frontiers[i] = new_frontier
        hope -= lost_hope
    result = get_frontiers(feild, n, m, p)
    return [len(ele) for ele in result]


def main():
    d = {str(i): i for i in range(1, 10)}
    d['.'] = 0
    d['#'] = -1
    n, m, p = map(int, input().split())
    speeds = list(map(int, input().split()))
    feild = []
    for i in range(n):
        feild.append(list(map(d.get, input())))
    result = solve(speeds, feild, n, m, p)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()