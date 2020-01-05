from n_queens import NQueens


def main():
    print('.: N-Queens Problem :.')
    size = int(input('Please enter the size of board: '))
    n_queens = NQueens(size)
    dfs_solutions = n_queens.solve_dfs()
    bfs_solutions = n_queens.solve_bfs()
    for i, solution in enumerate(dfs_solutions):
        print('DFS Solution %d:' % (i + 1))
        n_queens.print(solution)
    for i, solution in enumerate(bfs_solutions):
        print('BFS Solution %d:' % (i + 1))
        n_queens.print(solution)
    print('Total DFS solutions: %d' % len(dfs_solutions))
    print('Total BFS solutions: %d' % len(bfs_solutions))


if __name__ == '__main__':
    main()
