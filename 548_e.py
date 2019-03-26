# import time
import itertools
import copy

def delete_node(children, node):
    for v in children:
        v.discard(node)

def find_longest_path(children, clubs, frontier):
    clubs_visited = []
    result = 0
    while frontier:
        ele = frontier.pop()
        if ele is None:
            clubs_visited.pop()
        else:
            frontier.append(None)
            frontier.extend(filter(lambda x: clubs[x] not in clubs_visited,
                children[ele]))
            clubs_visited.append(clubs[ele])
            result = max(result, len(clubs_visited))
    return result

def solve(potentials, clubs, dies, m, n, d):
    potential_index = {}
    for i, p in enumerate(potentials):
        if p in potential_index:
            potential_index[p].add(i)
        else:
            potential_index[p] = set([i])
    # print('p_index:')
    # print(potential_index)
    # print('club_index')
    # print(club_index)
    childrens = [set() for i in range(n)]
    potential_max = max(potential_index.keys())
    # print('p_max:', potential_max)
    for p in range(potential_max):
        for a, b in filter(lambda x: clubs[x[0]] != clubs[x[1]],
                itertools.product(potential_index.get(p, {}), potential_index.get(p + 1, {}))):
            # print(a, b)
            childrens[a].add(b)
    result = []
    # print('children:')
    # print(childrens)
    potentials_0 = potential_index[0]
    for i in range(d):
        delete_node(childrens, dies[i])
        potentials_0.discard(dies[i])
        sub_result = find_longest_path(childrens, clubs, list(potentials_0))
        result.append(sub_result)
    return result

def main():
    # Deal with input.
    n , m = map(int, input().split())
    potentials = list(map(int, input().split()))
    clubs = list(map(int, input().split()))
    d = int(input())
    dies = []
    for i in range(d):
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
    pass

if __name__ == "__main__":
    main()