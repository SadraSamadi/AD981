def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, u, v):
    i = find(parent, u)
    j = find(parent, v)
    if rank[i] < rank[j]:
        parent[i] = j
    elif rank[i] > rank[j]:
        parent[j] = i
    else:
        parent[j] = i
        rank[i] += 1


def kruskal(vertices, edges):
    edges.sort(key=lambda r: r[2], reverse=True)
    parent = [v for v in range(vertices)]
    rank = [0] * vertices
    mst = []
    while len(mst) < vertices - 1:
        u, v, w = edges.pop()
        i = find(parent, u)
        j = find(parent, v)
        if i != j:
            mst.append([u, v, w])
            union(parent, rank, i, j)
    for u, v, w in mst:
        print('(%d) <- %d -> (%d)' % (u, w, v))


def main():
    print('Kruskal - Minimum Spanning Tree')
    kruskal(6, [
        [0, 1, 5],
        [0, 2, 4],
        [0, 4, 5],
        [1, 2, 3],
        [1, 3, 4],
        [2, 3, 4],
        [2, 4, 3],
        [3, 4, 6],
        [3, 5, 2],
        [4, 5, 4]
    ])


if __name__ == '__main__':
    main()
