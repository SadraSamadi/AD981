from math import pow, ceil, log2


def shift(n, zeros):
    s = str(n)
    for _ in range(zeros):
        s += '0'
    return int(s)


def _multiply(a, b, length, zeros):
    if length == 1:
        p = int(a) * int(b)
        return shift(p, zeros)
    middle = length // 2
    a_left = a[:middle]
    a_right = a[middle:]
    b_left = b[:middle]
    b_right = b[middle:]
    p1 = _multiply(a_left, b_left, middle, length)
    p2 = _multiply(a_left, b_right, middle, middle)
    p3 = _multiply(a_right, b_left, middle, middle)
    p4 = _multiply(a_right, b_right, middle, 0)
    return shift(p1 + p2 + p3 + p4, zeros)


def multiply(a, b):
    length = int(pow(2, ceil(log2(max(len(a), len(b))))))
    while len(a) < length:
        a = '0' + a
    while len(b) < length:
        b = '0' + b
    return _multiply(a, b, length, 0)


def main():
    a = input('Please enter the first number: ')
    b = input('Please enter the second number: ')
    result = multiply(a, b)
    print('Result:', result)


if __name__ == '__main__':
    main()
