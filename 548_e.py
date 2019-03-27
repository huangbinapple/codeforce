# import time
import itertools

def delete_node(children, node):
    for v in children:
        v.discard(node)

def find_longest_path(children, clubs, frontier):
    clubs_visited = []
    path = []
    top_path = []
    result = [0, 0]
    while frontier:
        ele = frontier.pop()
        if ele is None:
            clubs_visited.pop()
            path.pop()
        else:
            frontier.append(None)
            new_nodes = list(filter(lambda x: clubs[x] not in clubs_visited, children[ele]))
            frontier.extend(new_nodes)
            clubs_visited.append(clubs[ele])
            path.append(ele)
            if not new_nodes:
                # print('ya')
                if len(clubs_visited) > result[0]:
                    top_path = path.copy()
                result.append(len(clubs_visited))
                result.sort(reverse=True)
                result.pop()
    return result, top_path

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
    potentials_index_key = sorted(list(potential_index.keys()))
    for i in range(1, len(potentials_index_key)):
        last_po, current_po = potentials_index_key[i - 1], potentials_index_key[i]
        if last_po == current_po - 1:
            for a, b in filter(lambda x: clubs[x[0]] != clubs[x[1]],
                    itertools.product(potential_index[last_po], potential_index[current_po])):
                childrens[a].add(b)
    result = []
    top_two_length, top_path = [0, 0], []
    potentials_0 = potential_index[0]
    for i in range(d):
        delete_node(childrens, dies[i])
        potentials_0.discard(dies[i])
        try:
            die_index = top_path.index(dies[i])
        except ValueError:
            die_index = -1
        if top_path and die_index == -1:
            pass
        elif top_path and die_index >= top_two_length[1]:
            top_two_length[0] = die_index
            top_path = top_path[:die_index]
        else:
            top_two_length, top_path = find_longest_path(childrens, clubs, list(potentials_0))
        result.append(top_two_length[0])
    return result

def main():
    # Deal with input.
    n , m = map(int, input().split())
    potentials = list(map(int, input().split()))
    clubs = list(map(int, input().split()))
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
    n, m = 1000, 1000
    potentials = list(range(n))
    clubs = list(range(m))
    dies = list(reversed(range(1, n + 1)))
    d = n
    # tick = time.time()
    result = solve(potentials, clubs, dies, m, n, d)
    # tock = time.time()
    # Deal with output.
    for ele in result:
        print(ele)
    # Printe time.
    # print('T:', round(tock - tick ,5))


if __name__ == "__main__":
    main()