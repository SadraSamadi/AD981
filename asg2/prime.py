import math
import time
import random


def is_prime_v1(n):
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def is_prime_v2(n):
    if n % 2 == 0:
        return False
    for k in range(3, n, 2):
        if n % k == 0:
            return False
    return True


def is_prime_v3(n):
    if n % 2 == 0:
        return False
    stop = math.ceil(n / 2)
    for k in range(3, stop, 2):
        if n % k == 0:
            return False
    return True


def is_prime_v4(n):
    if n % 2 == 0:
        return False
    sqrt = math.sqrt(n)
    stop = math.ceil(sqrt)
    for k in range(3, stop, 2):
        if n % k == 0:
            return False
    return True


def profile(f, a):
    b = time.time()
    f(a)
    e = time.time()
    return (e - b) * 1000


def main():
    data = [[0 for _ in range(4)] for _ in range(10)]
    for i in range(10):
        for j in range(100):
            a = 100000 + 9990000 * i
            b = 100000 + 9990000 * (i + 1)
            n = random.randint(a, b)
            data[i][0] += profile(is_prime_v1, n)
            data[i][1] += profile(is_prime_v2, n)
            data[i][2] += profile(is_prime_v3, n)
            data[i][3] += profile(is_prime_v4, n)
        for j in range(4):
            data[i][j] /= 100
    for i in range(10):
        print('%d-%d\t' % (100000 + 9990000 * i, 100000 + 9990000 * (i + 1)), end='')
        for j in range(4):
            print('%f\t' % data[i][j], end='')
        print()


if __name__ == '__main__':
    main()
