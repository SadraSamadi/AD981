import math


def is_perfect_square(n):
    sr = math.sqrt(n)
    sr = math.floor(sr)
    return n == sr ** 2


def is_fibonacci(n):
    p = 5 * n ** 2
    return is_perfect_square(p + 4) or is_perfect_square(p - 4)


def main():
    n = int(input('Please enter the number: '))
    if is_fibonacci(n):
        print('%d is a Fibonacci number.' % n)
    else:
        print('%d is not a Fibonacci number.' % n)


if __name__ == '__main__':
    main()
