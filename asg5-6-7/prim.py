import math


def min_key(vertices, key, mst):
    low = math.inf
    index = None
    for i in range(vertices):
        if key[i] < low and not mst[i]:
            low = key[i]
            index = i
    return index


def prim(vertices, graph):
    key = [math.inf] * vertices
    parent = [0] * vertices
    mst = [False] * vertices
    parent[0] = -1
    key[0] = 0
    for _ in range(vertices):
        u = min_key(vertices, key, mst)
        mst[u] = True
        for v in range(vertices):
            if 0 < graph[u][v] < key[v] and not mst[v]:
                key[v] = graph[u][v]
                parent[v] = u
    for i in range(1, vertices):
        print('(%d) <- %d -> (%d)' % (parent[i], graph[i][parent[i]], i))


def main():
    print('Prim - Minimum Spanning Tree')
    prim(6, [
        [0, 5, 4, 0, 5, 0],
        [5, 0, 3, 4, 0, 0],
        [4, 3, 0, 4, 3, 0],
        [0, 4, 4, 0, 6, 2],
        [5, 0, 3, 6, 0, 4],
        [0, 0, 0, 2, 4, 0]
    ])


if __name__ == '__main__':
    main()
