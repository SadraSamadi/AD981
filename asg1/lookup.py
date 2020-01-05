lookup = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
    [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
    [0, 6, 12, 18, 24, 30, 36, 42, 48, 54],
    [0, 7, 14, 21, 28, 35, 42, 49, 56, 63],
    [0, 8, 16, 24, 32, 40, 48, 56, 64, 72],
    [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]
]


def multiply(a, b):
    n = str(int(abs(a)))
    m = str(int(abs(b)))
    n_len = len(n)
    m_len = len(m)
    t = [[0 for _ in range(n_len + m_len)] for _ in range(m_len)]
    for i in range(m_len):
        c = 0
        u = int(m[m_len - i - 1])
        for j in range(n_len):
            v = int(n[n_len - j - 1])
            p = lookup[u][v] + c
            t[i][n_len + m_len - j - i - 1] = p % 10
            c = int(p / 10)
        t[i][m_len - i - 1] = c
    s = ''
    c = 0
    for i in range(n_len + m_len):
        p = c
        for j in range(m_len):
            p = p + t[j][n_len + m_len - i - 1]
        s = str(p % 10) + s
        c = int(p / 10)
    if a < 0 <= b or b < 0 <= a:
        return -int(s)
    else:
        return int(s)


def complex_multiply(a, b):
    re = multiply(a.real, b.real) - multiply(a.imag, b.imag)
    im = multiply(a.real, b.imag) + multiply(a.imag, b.real)
    return complex(re, im)


def main():
    print('Multiplication - Lookup Table')
    a = complex(input('Please enter the first number (x+yj): '))
    b = complex(input('Please enter the second number (x+yj): '))
    print('The result is:', complex_multiply(a, b))


if __name__ == '__main__':
    main()
