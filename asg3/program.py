import random
import time


def evaluate_v1(x, a):
    n = len(a)
    s = a[0]
    for i in range(1, n):
        s += a[i] * x ** i
    return s


def evaluate_v2(x, a):
    n = len(a)
    s = a[0]
    t = 1
    for i in range(1, n):
        t *= x
        s += a[i] * t
    return s


def evaluate_v3(x, a):
    n = len(a)
    s = a[n - 1]
    for i in range(n - 2, -1, -1):
        s = s * x + a[i]
    return s


def profile(f, *args):
    b = time.time()
    f(*args)
    e = time.time()
    return (e - b) * 10 ** 6


def main():
    data = [[0] * 3 for _ in range(10)]
    for i in range(10):
        for _ in range(10):
            x = random.randint(-1000, 1000)
            a = [random.randint(-1000, 1000) for _ in range(100 + 100 * i)]
            data[i][0] += profile(evaluate_v1, x, a)
            data[i][1] += profile(evaluate_v2, x, a)
            data[i][2] += profile(evaluate_v3, x, a)
        for j in range(3):
            data[i][j] /= 10
    for i in range(10):
        print('%5d' % (100 + 100 * i), end='')
        for j in range(3):
            print('%10.2f' % data[i][j], end='')
        print()


if __name__ == '__main__':
    main()
