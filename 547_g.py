# import time

def set_color(edge, colors, color):
    if edge in colors:
        colors[edge] = color
    else:
        colors[(edge[1], edge[0])] = color

def set_node_color(node, parent, parent_color, index, bad_nodes, colors):
    is_bad_node = node in bad_nodes
    color = 1
    for child_node in (child for child in index[node] if child != parent):
        if color == parent_color:
            color += 1
        new_color = parent_color if is_bad_node else color
        color += 1
        set_color((node, child_node), colors, new_color)
        set_node_color(child_node, node, new_color, index, bad_nodes, colors)

def solve(n, k, edges):
    # print('k:', k)
    colors = {edge: None for edge in edges}
    index = {i : [] for i in range(1, n + 1)}
    for a, b in edges:
        index[a].append(b)
        index[b].append(a)
    # for kk, v in index.items():
        # print(kk, v)
    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda x: len(index[x]), reverse=True)
    # print(nodes)
    bad_nodes = set(nodes[:k])
    # print('bad nodes:', bad_nodes)
    set_node_color(nodes[k], None, None, index, bad_nodes, colors)
    result = []
    for a, b in edges:
        if (a, b) in colors:
            result.append(colors[(a, b)])
        else:
            result.append(colors[(b, a)])
    return result

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    # tick = time.time()
    result = solve(n, k, edges)
    # print('result:', result)
    print(len(set(result)))
    print(' '.join(map(str, result)))
    # tock = time.time()
    # print('T:', round(tock - tick, 5))

if __name__ == "__main__":
    main()