def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print('(%d) -> (%d)' % (a, c))
        hanoi(n - 1, b, c, a)


def main():
    n = int(input('Please enter the number of disks: '))
    hanoi(n, 1, 2, 3)
    print('Total moves:', 2 ** n - 1)


if __name__ == '__main__':
    main()
