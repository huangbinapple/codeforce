def get_frontiers(feild, n, m, p):
    # print(feild)
    # print(n, m)
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
    # print('In go:', player_id, frontier, n_turn)
    while n_turn and frontier:
        n_turn -= 1
        new_frontier = []
        for i, j in frontier:
            for d_i, d_j in (-1, 0), (1, 0), (0, 1), (0, -1):
                # check boarder.
                new_i, new_j = i + d_i, j + d_j
                if new_i < 0 or new_j < 0 or new_i > n - 1 or new_j > m - 1:
                    # DEBUG: should update loop variable `frontier` here before continue.
                    frontier = []
                    continue
                new_space = feild[new_i][new_j]
                if new_space == 0:
                    feild[new_i][new_j] = player_id
                    new_frontier.append((new_i, new_j))
        frontier = new_frontier
                # print('haha:', frontier)
        # print('player:', player_id)

        # for ele in feild:
            # print(ele)
    # print('Got new frontier:', frontier)
    return frontier

def solve(speeds, feild, n, m):
    frontiers = get_frontiers(feild, n, m, len(speeds))
    # print('f:', frontiers)
    hope = True
    while hope:
        hope = False
        for i in range(len(speeds)):
            n_turn = speeds[i]
            frontier = frontiers[i]
            new_frontier = go(i + 1, frontier, n_turn, feild, n, m)
            # print('i:', i)
            # print(new_frontier)
            if new_frontier:
                hope = True
            frontiers[i] = new_frontier
    result = get_frontiers(feild, n, m, len(speeds))
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
    # for ele in feild:
        # print(ele)
    result = solve(speeds, feild, n, m)
    print(' '.join(map(str, result)))
    # for ele in feild:
        # print(ele)

if __name__ == "__main__":
    main()